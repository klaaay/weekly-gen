#!/usr/bin/env python3
import asyncio
import contextlib
import os
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Optional, Dict, Any, List


def utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


@dataclass
class RunState:
    running: bool = False
    last_started_at: Optional[str] = None
    last_finished_at: Optional[str] = None
    last_returncode: Optional[int] = None
    last_duration_sec: Optional[float] = None
    last_log_file: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class JobScheduler:
    """Periodically runs `python main.py -w 8 --all` in background."""

    def __init__(
        self,
        interval_seconds: int = 300,
        workdir: str = ".",
        log_dir: str = os.path.join("outputs", "service_logs"),
        command: Optional[List[str]] = None,
    ) -> None:
        self.interval_seconds = interval_seconds
        self.workdir = workdir
        self.log_dir = log_dir
        # Default to running the module from src
        self.command = command or [sys.executable, "-m", "src.main", "-w", "8", "--all"]

        # internal state
        self._state = RunState()
        self._lock = asyncio.Lock()
        self._task: Optional[asyncio.Task] = None
        self._stop_event = asyncio.Event()

        # ensure dirs exist
        ensure_dir(self.log_dir)
        ensure_dir(os.path.join(self.workdir, "outputs"))

    @property
    def state(self) -> RunState:
        return self._state

    async def run_once(self) -> Dict[str, Any]:
        if self._lock.locked():
            return {"ok": False, "message": "job already running", "state": self._state.to_dict()}

        async with self._lock:
            self._state.running = True
            self._state.last_started_at = utcnow_iso()
            self._state.last_finished_at = None
            self._state.last_returncode = None
            self._state.last_duration_sec = None
            log_path = os.path.join(self.log_dir, f"run-{datetime.now().strftime('%Y%m%d-%H%M%S')}.log")
            self._state.last_log_file = log_path

            start = asyncio.get_event_loop().time()

            # open log file and run subprocess
            os.makedirs(os.path.dirname(log_path), exist_ok=True)
            with open(log_path, "w", encoding="utf-8") as logf:
                logf.write(f"[start] {self._state.last_started_at}\n")
                logf.write(f"[cmd] {' '.join(self.command)}\n")
                logf.flush()

                proc = await asyncio.create_subprocess_exec(
                    *self.command,
                    cwd=self.workdir,
                    stdout=logf,
                    stderr=logf,
                )

                rc = await proc.wait()

                finished = utcnow_iso()
                duration = asyncio.get_event_loop().time() - start
                self._state.running = False
                self._state.last_finished_at = finished
                self._state.last_returncode = rc
                self._state.last_duration_sec = round(duration, 3)

                logf.write(f"\n[finish] {finished} rc={rc} duration={self._state.last_duration_sec}s\n")

            return {"ok": True, "returncode": rc, "state": self._state.to_dict()}

    async def _loop(self) -> None:
        # staggered, interval measured from end of run
        while not self._stop_event.is_set():
            try:
                await self.run_once()
            except Exception as e:  # keep loop alive
                # best-effort logging to a daily file
                try:
                    ensure_dir(self.log_dir)
                    with open(os.path.join(self.log_dir, "scheduler-errors.log"), "a", encoding="utf-8") as ef:
                        ef.write(f"[{utcnow_iso()}] loop error: {e}\n")
                except Exception:
                    pass

            try:
                await asyncio.wait_for(self._stop_event.wait(), timeout=self.interval_seconds)
            except asyncio.TimeoutError:
                continue

    def start(self) -> None:
        if self._task is None or self._task.done():
            self._stop_event.clear()
            self._task = asyncio.create_task(self._loop(), name="weekly-gen-scheduler")

    async def stop(self) -> None:
        self._stop_event.set()
        task = self._task
        if task is not None:
            try:
                await asyncio.wait_for(task, timeout=10)
            except asyncio.TimeoutError:
                task.cancel()
                with contextlib.suppress(Exception):
                    await task
