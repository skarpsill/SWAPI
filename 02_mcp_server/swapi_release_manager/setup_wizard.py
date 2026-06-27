"""End-user installation wizard for SOLIDWORKS API MCP Server."""

from __future__ import annotations

import os
import queue
import shutil
import sys
import threading
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from .mcp_config import (
    default_vscode_config,
    default_vscodium_config,
    write_vscode_config,
    write_vscodium_config,
)
from .postgres_tools import (
    install_postgres_silent,
    is_database_populated,
    is_postgres_installed,
    restore_dump,
    wait_for_postgres_service,
)

_INSTALL_DIR = Path(
    os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")
) / "Programs" / "SolidWorksApiMcp"

_DATABASE = "solidworks_api"
_DB_USER = "postgres"
_DB_HOST = "localhost"
_DB_PORT = 5432
_API_VERSION = "2024"

_TITLE = "SOLIDWORKS API MCP — Установка"
_W, _H = 620, 500


def _bundle_dir() -> Path:
    """Directory containing swapi-setup.exe and sibling files."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).parent


# ── pages ─────────────────────────────────────────────────────────────────────

class _WelcomePage(ttk.Frame):
    def __init__(self, master: tk.Widget, on_next) -> None:
        super().__init__(master)

        ttk.Label(
            self,
            text="SOLIDWORKS API MCP Server",
            font=("Segoe UI", 16, "bold"),
        ).pack(pady=(48, 6))
        ttk.Label(self, text="Мастер установки", font=("Segoe UI", 11)).pack()
        ttk.Separator(self, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=48, pady=20)

        msg = (
            "Этот мастер установит:\n\n"
            "  •  MCP-сервер SOLIDWORKS API\n"
            "  •  База данных SolidWorks API 2024 (PostgreSQL)\n"
            "  •  Настройки MCP для VS Code и VS Codium\n\n"
            "Если PostgreSQL 18 не установлен, он будет\n"
            "установлен автоматически из комплекта поставки."
        )
        ttk.Label(self, text=msg, justify=tk.LEFT, font=("Segoe UI", 10)).pack(
            padx=48, anchor=tk.W
        )

        btn_frame = ttk.Frame(self)
        btn_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=48, pady=24)
        ttk.Button(btn_frame, text="Далее →", command=on_next, width=14).pack(
            side=tk.RIGHT
        )


class _PasswordPage(ttk.Frame):
    def __init__(self, master: tk.Widget, on_install) -> None:
        super().__init__(master)
        self._on_install = on_install

        ttk.Label(
            self,
            text="Пароль администратора PostgreSQL",
            font=("Segoe UI", 13, "bold"),
        ).pack(pady=(40, 6))
        ttk.Label(
            self,
            text=(
                "Придумайте пароль для пользователя postgres.\n"
                "Он понадобится при обслуживании базы данных."
            ),
            font=("Segoe UI", 10),
            justify=tk.CENTER,
        ).pack(pady=(0, 24))

        form = ttk.Frame(self)
        form.pack(padx=72, fill=tk.X)

        ttk.Label(form, text="Пароль:", width=16, anchor=tk.W).grid(
            row=0, column=0, sticky=tk.W, pady=8
        )
        self._pwd1 = tk.StringVar()
        ttk.Entry(form, textvariable=self._pwd1, show="•", width=30).grid(
            row=0, column=1, sticky=tk.EW, pady=8
        )

        ttk.Label(form, text="Повторите:", width=16, anchor=tk.W).grid(
            row=1, column=0, sticky=tk.W, pady=8
        )
        self._pwd2 = tk.StringVar()
        ttk.Entry(form, textvariable=self._pwd2, show="•", width=30).grid(
            row=1, column=1, sticky=tk.EW, pady=8
        )
        form.columnconfigure(1, weight=1)

        self._error_label = ttk.Label(self, text="", foreground="red", font=("Segoe UI", 9))
        self._error_label.pack(pady=(10, 0))

        btn_frame = ttk.Frame(self)
        btn_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=48, pady=24)
        ttk.Button(btn_frame, text="Установить", command=self._validate, width=14).pack(
            side=tk.RIGHT
        )

    def _validate(self) -> None:
        p1, p2 = self._pwd1.get(), self._pwd2.get()
        if len(p1) < 4:
            self._error_label.config(text="Пароль должен содержать не менее 4 символов.")
            return
        if p1 != p2:
            self._error_label.config(text="Пароли не совпадают. Попробуйте снова.")
            return
        self._error_label.config(text="")
        self._on_install(p1)


class _ProgressPage(ttk.Frame):
    def __init__(self, master: tk.Widget) -> None:
        super().__init__(master)

        ttk.Label(self, text="Установка...", font=("Segoe UI", 13, "bold")).pack(
            pady=(28, 10)
        )

        log_frame = ttk.Frame(self)
        log_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 8))
        self._text = tk.Text(
            log_frame,
            wrap=tk.WORD,
            state=tk.DISABLED,
            font=("Consolas", 9),
            background="#1e1e1e",
            foreground="#d4d4d4",
            relief=tk.FLAT,
        )
        scroll = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=self._text.yview)
        self._text.configure(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self._text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self._finish_btn = ttk.Button(
            self, text="Завершить", command=None, width=14, state=tk.DISABLED
        )
        self._finish_btn.pack(side=tk.BOTTOM, anchor=tk.E, padx=48, pady=20)

    def append(self, msg: str) -> None:
        self._text.configure(state=tk.NORMAL)
        self._text.insert(tk.END, msg + "\n")
        self._text.see(tk.END)
        self._text.configure(state=tk.DISABLED)

    def set_finish_command(self, cmd) -> None:
        self._finish_btn.configure(command=cmd, state=tk.NORMAL)


# ── wizard ─────────────────────────────────────────────────────────────────────

class SetupWizard(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title(_TITLE)
        self.geometry(f"{_W}x{_H}")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self._installing = False
        self._log_queue: queue.Queue[str] = queue.Queue()
        self._current_page: ttk.Frame | None = None

        self._show_welcome()
        self.after(100, self._drain_log)

    # ── navigation ────────────────────────────────────────────────────────

    def _switch(self, page: ttk.Frame) -> None:
        if self._current_page is not None:
            self._current_page.pack_forget()
        self._current_page = page
        page.pack(fill=tk.BOTH, expand=True)

    def _show_welcome(self) -> None:
        self._switch(_WelcomePage(self, on_next=self._show_password))

    def _show_password(self) -> None:
        self._switch(_PasswordPage(self, on_install=self._start_install))

    def _start_install(self, password: str) -> None:
        self._installing = True
        self._progress = _ProgressPage(self)
        self._switch(self._progress)
        threading.Thread(
            target=self._run_install, args=(password,), daemon=True
        ).start()

    # ── install thread ────────────────────────────────────────────────────

    def _log(self, msg: str) -> None:
        self._log_queue.put(msg)

    def _drain_log(self) -> None:
        while True:
            try:
                msg = self._log_queue.get_nowait()
                self._progress.append(msg) if hasattr(self, "_progress") else None
            except queue.Empty:
                break
        self.after(100, self._drain_log)

    def _run_install(self, password: str) -> None:
        try:
            bundle = _bundle_dir()
            self._step_postgres(bundle, password)
            self._step_restore_db(bundle, password)
            self._step_copy_exe(bundle)
            self._step_mcp_config()
            self._log("\n✓  Установка завершена успешно!")
            self.after(0, lambda: self.title(_TITLE + " — Готово"))
            self.after(0, lambda: self._progress.set_finish_command(self.destroy))
        except Exception as exc:
            self._log(f"\n✗  Ошибка: {exc}")
            self.after(0, lambda: messagebox.showerror("Ошибка установки", str(exc)))
            self.after(0, lambda: self._progress.set_finish_command(self.destroy))
        finally:
            self._installing = False

    def _step_postgres(self, bundle: Path, password: str) -> None:
        self._log("── Проверка PostgreSQL 18 ────────────────────────")
        if is_postgres_installed():
            self._log("✓  PostgreSQL 18 уже установлен")
            return
        installers = sorted(bundle.glob("postgresql-18*.exe"))
        if not installers:
            raise FileNotFoundError(
                "PostgreSQL 18 не найден, а установочный файл\n"
                "postgresql-18*.exe отсутствует рядом с setup.exe."
            )
        self._log(f"Запуск установщика: {installers[0].name}")
        install_postgres_silent(installers[0], password, self._log)
        self._log("Ожидание запуска службы PostgreSQL...")
        wait_for_postgres_service(timeout=120, log=self._log)
        self._log("✓  PostgreSQL 18 установлен и запущен")

    def _step_restore_db(self, bundle: Path, password: str) -> None:
        self._log("\n── Восстановление базы данных ───────────────────")
        if is_database_populated(
            database=_DATABASE,
            user=_DB_USER,
            host=_DB_HOST,
            port=_DB_PORT,
            password=password,
        ):
            self._log("✓  База данных уже установлена — пропуск восстановления")
            return
        dumps = sorted(bundle.glob("solidworks_api_*.dump"))
        if not dumps:
            raise FileNotFoundError(
                "Файл solidworks_api_*.dump не найден рядом с setup.exe."
            )
        self._log(f"Дамп: {dumps[0].name}")
        restore_dump(
            dump_path=dumps[0],
            database=_DATABASE,
            user=_DB_USER,
            host=_DB_HOST,
            port=_DB_PORT,
            drop_existing=False,
            password=password,
            log=self._log,
        )
        self._log("✓  База данных восстановлена")

    def _step_copy_exe(self, bundle: Path) -> None:
        self._log("\n── Установка MCP-сервера ─────────────────────────")
        src = bundle / "swapi-mcp-server.exe"
        if not src.exists():
            raise FileNotFoundError(f"swapi-mcp-server.exe не найден: {src}")
        _INSTALL_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, _INSTALL_DIR / "swapi-mcp-server.exe")
        self._log(f"✓  Установлен в {_INSTALL_DIR}")

    def _step_mcp_config(self) -> None:
        self._log("\n── Настройка MCP-клиентов ───────────────────────")
        exe = _INSTALL_DIR / "swapi-mcp-server.exe"
        db_url = f"postgresql://{_DB_USER}@{_DB_HOST}:{_DB_PORT}/{_DATABASE}"
        env = {
            "SWAPI_DATABASE_URL": db_url,
            "SWAPI_DEFAULT_VERSION": _API_VERSION,
        }

        vscode_path = default_vscode_config()
        write_vscode_config(vscode_path, exe, env)
        self._log(f"✓  VS Code:    {vscode_path}")

        vscodium_path = default_vscodium_config()
        write_vscodium_config(vscodium_path, exe, env)
        self._log(f"✓  VS Codium:  {vscodium_path}")

    # ── close guard ───────────────────────────────────────────────────────

    def _on_close(self) -> None:
        if self._installing:
            messagebox.showwarning(_TITLE, "Идёт установка. Дождитесь завершения.")
            return
        self.destroy()


def main() -> None:
    wizard = SetupWizard()
    wizard.mainloop()
