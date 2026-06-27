"""Tkinter GUI for Windows release management."""

from __future__ import annotations

from pathlib import Path
import os
import queue
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from .installer import install_local_package
from .mcp_config import default_codex_config, default_vscode_config
from .paths import resolve_paths, resolve_under
from .postgres_tools import export_dump
from .publisher import publish_github_release
from .release_builder import build_server_package


class ReleaseManagerApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("SOLIDWORKS API MCP Release Manager")
        self.geometry("980x720")
        self.paths = resolve_paths()
        self.messages: queue.Queue[str] = queue.Queue()
        self.busy = False

        self._build_vars()
        self._build_ui()
        self.after(100, self._drain_log)

    def _build_vars(self) -> None:
        self.repo_root = tk.StringVar(value=str(self.paths.repo_root))
        self.version = tk.StringVar(value="0.1.0-alpha.1")
        self.api_version = tk.StringVar(value="2024")
        self.database = tk.StringVar(value="solidworks_api")
        self.database_user = tk.StringVar(value="postgres")
        self.database_host = tk.StringVar(value="localhost")
        self.database_port = tk.IntVar(value=5432)
        self.dump_path = tk.StringVar(value=str(self.paths.parsing_root / "release-assets" / "solidworks_api_2024.dump"))
        _pg = self.paths.postgresql_installer
        self.pg_installer_path = tk.StringVar(value=str(_pg) if _pg else "")
        self.dump_output_dir = tk.StringVar(value=str(self.paths.parsing_root / "release-assets"))
        self.package_output_dir = tk.StringVar(value=str(self.paths.product_root / "dist"))
        self.package_path = tk.StringVar(value=str(self.paths.product_root / "dist" / "solidworks-api-mcp-0.1.0-alpha.1-windows-x64.zip"))
        self.package_dir = tk.StringVar(value=str(self.paths.product_root / "dist" / "solidworks-api-mcp-0.1.0-alpha.1-windows-x64"))
        self.install_dir = tk.StringVar(value=str(Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "Programs" / "SolidWorksApiMcp"))
        self.skip_restore = tk.BooleanVar(value=False)
        self.configure_codex = tk.BooleanVar(value=True)
        self.configure_vscode = tk.BooleanVar(value=False)
        self.codex_config = tk.StringVar(value=str(default_codex_config()))
        self.vscode_config = tk.StringVar(value=str(default_vscode_config()))
        self.github_tag = tk.StringVar(value="v0.1.0-alpha.1")
        self.github_title = tk.StringVar(value="")
        self.github_draft = tk.BooleanVar(value=True)

    def _build_ui(self) -> None:
        root_frame = ttk.Frame(self, padding=10)
        root_frame.pack(fill=tk.BOTH, expand=True)

        repo = ttk.LabelFrame(root_frame, text="Workspace")
        repo.pack(fill=tk.X)
        self._path_row(repo, "Repository root", self.repo_root, self._choose_repo_root)

        notebook = ttk.Notebook(root_frame)
        notebook.pack(fill=tk.BOTH, expand=True, pady=(10, 8))
        self._build_export_tab(notebook)
        self._build_package_tab(notebook)
        self._build_install_tab(notebook)
        self._build_publish_tab(notebook)

        log_frame = ttk.LabelFrame(root_frame, text="Log")
        log_frame.pack(fill=tk.BOTH, expand=True)
        self.log = tk.Text(log_frame, height=12, wrap=tk.WORD)
        self.log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=self.log.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.log.configure(yscrollcommand=scroll.set)

    def _build_export_tab(self, notebook: ttk.Notebook) -> None:
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="Export Dump")
        self._db_fields(frame)
        self._entry_row(frame, "API version", self.api_version)
        self._path_row(frame, "Output directory", self.dump_output_dir, lambda: self._choose_dir(self.dump_output_dir))
        ttk.Button(frame, text="Export PostgreSQL Dump", command=self.export_dump).pack(anchor=tk.W, pady=10)

    def _build_package_tab(self, notebook: ttk.Notebook) -> None:
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="Build Package")
        self._entry_row(frame, "Package version", self.version)
        self._entry_row(frame, "API version", self.api_version)
        self._path_row(frame, "Database dump", self.dump_path, lambda: self._choose_file(self.dump_path, [("Dump files", "*.dump"), ("All files", "*.*")]))
        self._path_row(
            frame,
            "PG installer",
            self.pg_installer_path,
            lambda: self._choose_file(
                self.pg_installer_path,
                [("PostgreSQL installer", "postgresql-18*.exe"), ("All files", "*.*")],
            ),
        )
        ttk.Label(frame, text="  (необязательно) postgresql-18*.exe для бандлинга в пакет", foreground="gray", font=("Segoe UI", 8)).pack(anchor=tk.W, padx=4)
        self._path_row(frame, "Output directory", self.package_output_dir, lambda: self._choose_dir(self.package_output_dir))
        ttk.Button(frame, text="Build Release Package", command=self.build_package).pack(anchor=tk.W, pady=10)

    def _build_install_tab(self, notebook: ttk.Notebook) -> None:
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="Install Locally")
        self._path_row(frame, "Package directory", self.package_dir, lambda: self._choose_dir(self.package_dir))
        self._path_row(frame, "Install directory", self.install_dir, lambda: self._choose_dir(self.install_dir))
        self._db_fields(frame)
        ttk.Checkbutton(frame, text="Skip database restore", variable=self.skip_restore).pack(anchor=tk.W, pady=(8, 0))
        ttk.Checkbutton(frame, text="Write Codex config", variable=self.configure_codex).pack(anchor=tk.W)
        self._path_row(frame, "Codex config", self.codex_config, lambda: self._choose_save(self.codex_config))
        ttk.Checkbutton(frame, text="Write VS Code MCP config", variable=self.configure_vscode).pack(anchor=tk.W)
        self._path_row(frame, "VS Code config", self.vscode_config, lambda: self._choose_save(self.vscode_config))
        ttk.Button(frame, text="Install Package Locally", command=self.install_package).pack(anchor=tk.W, pady=10)

    def _build_publish_tab(self, notebook: ttk.Notebook) -> None:
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="Publish")
        self._entry_row(frame, "Git tag", self.github_tag)
        self._entry_row(frame, "Release title", self.github_title)
        self._path_row(frame, "Package zip", self.package_path, lambda: self._choose_file(self.package_path, [("Zip files", "*.zip"), ("All files", "*.*")]))
        ttk.Checkbutton(frame, text="Draft release", variable=self.github_draft).pack(anchor=tk.W, pady=(8, 0))
        ttk.Button(frame, text="Publish GitHub Release", command=self.publish_release).pack(anchor=tk.W, pady=10)

    def _db_fields(self, frame: ttk.Frame) -> None:
        self._entry_row(frame, "Database", self.database)
        self._entry_row(frame, "User", self.database_user)
        self._entry_row(frame, "Host", self.database_host)
        self._entry_row(frame, "Port", self.database_port)

    def _entry_row(self, parent: ttk.Frame, label: str, var: tk.Variable) -> None:
        row = ttk.Frame(parent)
        row.pack(fill=tk.X, pady=3)
        ttk.Label(row, text=label, width=18).pack(side=tk.LEFT)
        ttk.Entry(row, textvariable=var).pack(side=tk.LEFT, fill=tk.X, expand=True)

    def _path_row(self, parent: ttk.Frame, label: str, var: tk.StringVar, command) -> None:
        row = ttk.Frame(parent)
        row.pack(fill=tk.X, pady=3)
        ttk.Label(row, text=label, width=18).pack(side=tk.LEFT)
        ttk.Entry(row, textvariable=var).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(row, text="Browse", command=command).pack(side=tk.LEFT, padx=(6, 0))

    def _choose_repo_root(self) -> None:
        self._choose_dir(self.repo_root)
        self.paths = resolve_paths(Path(self.repo_root.get()))

    def _choose_dir(self, var: tk.StringVar) -> None:
        selected = filedialog.askdirectory(initialdir=var.get() or str(self.paths.repo_root))
        if selected:
            var.set(selected)

    def _choose_file(self, var: tk.StringVar, filetypes) -> None:
        selected = filedialog.askopenfilename(initialdir=str(Path(var.get()).parent), filetypes=filetypes)
        if selected:
            var.set(selected)

    def _choose_save(self, var: tk.StringVar) -> None:
        selected = filedialog.asksaveasfilename(initialfile=Path(var.get()).name, initialdir=str(Path(var.get()).parent))
        if selected:
            var.set(selected)

    def _log(self, message: str) -> None:
        self.messages.put(message)

    def _drain_log(self) -> None:
        while True:
            try:
                message = self.messages.get_nowait()
            except queue.Empty:
                break
            self.log.insert(tk.END, message + "\n")
            self.log.see(tk.END)
        self.after(100, self._drain_log)

    def _run_task(self, label: str, fn) -> None:
        if self.busy:
            messagebox.showinfo("Busy", "Another task is already running.")
            return
        self.busy = True
        self._log(f"=== {label} ===")

        def worker() -> None:
            try:
                fn()
                self._log(f"=== {label} complete ===")
            except Exception as exc:
                self._log(f"ERROR: {exc}")
                self.after(0, lambda: messagebox.showerror(label, str(exc)))
            finally:
                self.busy = False

        threading.Thread(target=worker, daemon=True).start()

    def export_dump(self) -> None:
        self._run_task(
            "Export dump",
            lambda: export_dump(
                output_dir=resolve_under(self.paths.repo_root, self.dump_output_dir.get()),
                api_version=self.api_version.get(),
                database=self.database.get(),
                user=self.database_user.get(),
                host=self.database_host.get(),
                port=int(self.database_port.get()),
                log=self._log,
            ),
        )

    def build_package(self) -> None:
        def task() -> None:
            pg_installer_str = self.pg_installer_path.get().strip()
            zip_path = build_server_package(
                paths=self.paths,
                version=self.version.get(),
                api_version=self.api_version.get(),
                database_dump=Path(self.dump_path.get()).expanduser() if self.dump_path.get().strip() else None,
                postgresql_installer=Path(pg_installer_str).expanduser() if pg_installer_str else None,
                output_dir=resolve_under(self.paths.product_root, self.package_output_dir.get()),
                log=self._log,
            )
            self.after(0, lambda: self._set_package_paths(zip_path))

        self._run_task("Build package", task)

    def _set_package_paths(self, zip_path: Path) -> None:
        self.package_path.set(str(zip_path))
        self.package_dir.set(str(zip_path.with_suffix("")))

    def install_package(self) -> None:
        self._run_task(
            "Install package",
            lambda: install_local_package(
                package_dir=Path(self.package_dir.get()).expanduser(),
                install_dir=Path(self.install_dir.get()).expanduser(),
                database=self.database.get(),
                database_user=self.database_user.get(),
                database_host=self.database_host.get(),
                database_port=int(self.database_port.get()),
                api_version=self.api_version.get(),
                skip_database_restore=self.skip_restore.get(),
                configure_codex=self.configure_codex.get(),
                codex_config_path=Path(self.codex_config.get()).expanduser(),
                configure_vscode=self.configure_vscode.get(),
                vscode_config_path=Path(self.vscode_config.get()).expanduser(),
                log=self._log,
            ),
        )

    def publish_release(self) -> None:
        self._run_task(
            "Publish release",
            lambda: publish_github_release(
                repo_root=self.paths.repo_root,
                tag=self.github_tag.get(),
                title=self.github_title.get(),
                package_path=Path(self.package_path.get()).expanduser(),
                draft=self.github_draft.get(),
                log=self._log,
            ),
        )


def main() -> None:
    app = ReleaseManagerApp()
    app.mainloop()
