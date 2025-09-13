#!/usr/bin/env python3
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import os

from .scheduler import JobScheduler


class StatusModel(BaseModel):
    running: bool
    last_started_at: str | None
    last_finished_at: str | None
    last_returncode: int | None
    last_duration_sec: float | None
    last_log_file: str | None


def create_app() -> FastAPI:
    app = FastAPI(title="weekly-gen service", version="0.1.0")

    # config via env
    interval = int(os.getenv("TASK_INTERVAL_SECONDS", "300"))
    workdir = os.getenv("WORKDIR", ".")

    scheduler = JobScheduler(interval_seconds=interval, workdir=workdir)

    @app.on_event("startup")
    async def _on_startup() -> None:
        scheduler.start()

    @app.on_event("shutdown")
    async def _on_shutdown() -> None:
        await scheduler.stop()

    @app.get("/healthz")
    async def healthz():
        return {"status": "ok"}

    @app.get("/status", response_model=StatusModel)
    async def get_status():
        return scheduler.state.to_dict()

    @app.post("/run-now")
    async def run_now():
        res = await scheduler.run_once()
        if not res.get("ok"):
            return Response(content=res.get("message", "already running"), status_code=status.HTTP_409_CONFLICT)
        return res

    return app


app = create_app()

