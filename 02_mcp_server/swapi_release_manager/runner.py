"""Subprocess runner helpers with log streaming."""

from __future__ import annotations

from pathlib import Path
import subprocess
from typing import Callable, Sequence


LogFn = Callable[[str], None]


def run_command(args: Sequence[str | Path], cwd: Path, log: LogFn) -> None:
    printable = " ".join(str(arg) for arg in args)
    log(f"> {printable}")
    process = subprocess.Popen(
        [str(arg) for arg in args],
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    assert process.stdout is not None
    for line in process.stdout:
        log(line.rstrip())
    code = process.wait()
    if code:
        raise RuntimeError(f"Command failed with exit code {code}: {printable}")


def capture_command(args: Sequence[str | Path], cwd: Path, log: LogFn) -> str:
    printable = " ".join(str(arg) for arg in args)
    log(f"> {printable}")
    completed = subprocess.run(
        [str(arg) for arg in args],
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if completed.stdout:
        for line in completed.stdout.splitlines():
            log(line.rstrip())
    if completed.returncode:
        raise RuntimeError(f"Command failed with exit code {completed.returncode}: {printable}")
    return completed.stdout
