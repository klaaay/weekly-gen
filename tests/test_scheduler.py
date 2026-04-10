from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi.testclient import TestClient

from app.server import create_app
from app.scheduler import JobScheduler


def test_compute_next_daily_run_same_day_before_target():
    scheduler = JobScheduler(
        schedule_mode="daily",
        schedule_time="09:00",
        schedule_timezone="Asia/Shanghai",
    )

    now = datetime(2026, 4, 10, 8, 30, tzinfo=ZoneInfo("Asia/Shanghai"))
    result = scheduler._compute_next_run_at(now)

    assert result.isoformat() == "2026-04-10T09:00:00+08:00"


def test_compute_next_daily_run_next_day_after_target():
    scheduler = JobScheduler(
        schedule_mode="daily",
        schedule_time="09:00",
        schedule_timezone="Asia/Shanghai",
    )

    now = datetime(2026, 4, 10, 9, 1, tzinfo=ZoneInfo("Asia/Shanghai"))
    result = scheduler._compute_next_run_at(now)

    assert result.isoformat() == "2026-04-11T09:00:00+08:00"


def test_interval_mode_does_not_require_schedule_time():
    scheduler = JobScheduler(interval_seconds=300, schedule_mode="interval")

    assert scheduler.schedule_mode == "interval"
    assert scheduler.interval_seconds == 300


def test_status_exposes_daily_schedule_config(monkeypatch):
    monkeypatch.setenv("SCHEDULE_MODE", "daily")
    monkeypatch.setenv("SCHEDULE_TIME", "09:00")
    monkeypatch.setenv("SCHEDULE_TZ", "Asia/Shanghai")
    app = create_app()
    client = TestClient(app)

    response = client.get("/status")

    assert response.status_code == 200
    payload = response.json()
    assert payload["schedule_mode"] == "daily"
    assert payload["schedule_time"] == "09:00"
    assert payload["schedule_timezone"] == "Asia/Shanghai"
    assert payload["next_scheduled_at"]
