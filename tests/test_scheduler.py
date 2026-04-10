import json
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


def test_run_state_is_persisted_to_json(tmp_path):
    state_file = tmp_path / "service_state.json"
    scheduler = JobScheduler(
        schedule_mode="daily",
        schedule_time="09:00",
        schedule_timezone="Asia/Shanghai",
        state_file_path=str(state_file),
    )

    scheduler._state.last_started_at = "2026-04-11T09:00:00+08:00"
    scheduler._state.last_finished_at = "2026-04-11T09:02:00+08:00"
    scheduler._state.last_returncode = 0
    scheduler._state.last_duration_sec = 120.0
    scheduler._persist_state()

    payload = json.loads(state_file.read_text(encoding="utf-8"))
    assert payload["last_returncode"] == 0
    assert payload["last_duration_sec"] == 120.0


def test_scheduler_loads_persisted_state_and_recomputes_next_run(tmp_path):
    state_file = tmp_path / "service_state.json"
    state_file.write_text(
        json.dumps(
            {
                "running": True,
                "last_started_at": "2026-04-10T09:00:00+08:00",
                "last_finished_at": "2026-04-10T09:05:00+08:00",
                "last_returncode": 0,
                "last_duration_sec": 300.0,
                "last_log_file": "outputs/service_logs/run-20260410-090000.log",
                "schedule_mode": "daily",
                "schedule_time": "09:00",
                "schedule_timezone": "Asia/Shanghai",
                "next_scheduled_at": "2099-01-01T09:00:00+08:00",
            }
        ),
        encoding="utf-8",
    )

    scheduler = JobScheduler(
        schedule_mode="daily",
        schedule_time="09:00",
        schedule_timezone="Asia/Shanghai",
        state_file_path=str(state_file),
    )

    assert scheduler.state.running is False
    assert scheduler.state.last_returncode == 0
    assert scheduler.state.last_log_file == "outputs/service_logs/run-20260410-090000.log"
    assert scheduler.state.next_scheduled_at != "2099-01-01T09:00:00+08:00"
