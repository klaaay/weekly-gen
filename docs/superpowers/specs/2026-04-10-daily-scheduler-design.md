# Daily Scheduler Design

## Goal

Make the containerized `weekly-gen` service trigger the same logic as `POST /run-now` once per day at `09:00` in `Asia/Shanghai`, while keeping the existing manual trigger API available.

## Current State

- The service starts a FastAPI app from `app.server`.
- A background scheduler is created on startup.
- The scheduler currently only supports interval-based execution via `TASK_INTERVAL_SECONDS`.
- Docker Compose currently sets `TASK_INTERVAL_SECONDS=1200`, so the service runs every 20 minutes instead of at a fixed wall-clock time.
- The service is intended to be self-contained inside the container rather than depend on host cron.

## Requirements

- Run once per day at `09:00` in `Asia/Shanghai`.
- Reuse the same execution path as `/run-now`.
- Preserve the existing `/run-now` endpoint behavior.
- Preserve the existing interval mode for backward compatibility.
- Keep deployment simple: rebuild image and restart compose, without adding a second scheduler process.

## Options Considered

### Option 1: Extend the in-process scheduler

Add a scheduler mode that computes the next `09:00` execution time in a configured timezone and sleeps until then.

Pros:
- Smallest architectural change
- Reuses existing locking and run state handling
- Keeps container self-contained

Cons:
- Slightly more scheduler logic to maintain

### Option 2: Use host cron to call `/run-now`

Move the daily schedule out of the app and let the host invoke the API each morning.

Pros:
- Minimal code change in the app

Cons:
- Deployment depends on host configuration
- Breaks the self-contained container model
- Harder to reason about in environments beyond the current machine

### Option 3: Add a dedicated cron process inside the container

Use `cron` or `supercronic` alongside the FastAPI process.

Pros:
- Scheduling model is explicit

Cons:
- More moving parts
- More image and process management complexity
- Unnecessary for a single daily job

## Decision

Use Option 1.

The existing app already owns job state, locking, logging, and the manual trigger path. Extending the scheduler to support a daily mode is the lowest-risk way to match the requested behavior.

## Proposed Design

### Configuration

Add three environment variables:

- `SCHEDULE_MODE`
  - Allowed values: `interval`, `daily`
  - Default: `interval`
- `SCHEDULE_TIME`
  - Format: `HH:MM`
  - Used only when `SCHEDULE_MODE=daily`
  - Default: `09:00`
- `SCHEDULE_TZ`
  - IANA timezone string
  - Default: `Asia/Shanghai`

Keep `TASK_INTERVAL_SECONDS` for interval mode compatibility.

### Scheduler Behavior

The scheduler loop will branch by mode:

- `interval`
  - Preserve current behavior: run once, then wait `TASK_INTERVAL_SECONDS`
- `daily`
  - Compute the next occurrence of `SCHEDULE_TIME` in `SCHEDULE_TZ`
  - Wait until that timestamp unless stopped early
  - Trigger `run_once()`
  - Repeat by recalculating the next daily occurrence

The manual endpoint `POST /run-now` continues to call `run_once()` directly.

The existing lock in `run_once()` remains the source of truth that prevents overlapping runs.

### Status Visibility

Extend the status model with:

- `schedule_mode`
- `schedule_time`
- `schedule_timezone`
- `next_scheduled_at`

This allows callers to verify that the daily schedule is configured correctly after startup.

### Docker Compose

Update `docker-compose.yml` to use daily scheduling by default:

- `SCHEDULE_MODE=daily`
- `SCHEDULE_TIME=09:00`
- `SCHEDULE_TZ=Asia/Shanghai`

Remove or stop relying on `TASK_INTERVAL_SECONDS` in the compose default configuration.

### Error Handling

- Invalid `SCHEDULE_TIME` or `SCHEDULE_TZ` should fail fast on startup with a clear exception.
- Existing scheduler error logging should remain in place.
- If the process starts after `09:00`, the next run should be scheduled for the following day at `09:00`, not immediately.

## Files Expected To Change

- `app/server.py`
- `app/scheduler.py`
- `docker-compose.yml`
- `README.md`

## Verification Plan

1. Rebuild and start the container with `docker compose up -d --build`.
2. Confirm the container is `Up` in `docker compose ps`.
3. Call `GET /healthz` and confirm the service responds.
4. Call `GET /status` and confirm:
   - `schedule_mode` is `daily`
   - `schedule_time` is `09:00`
   - `schedule_timezone` is `Asia/Shanghai`
   - `next_scheduled_at` is populated
5. Trigger `POST /run-now` and confirm it still works.

## Non-Goals

- Supporting multiple scheduled times per day
- Adding calendar expressions such as cron syntax
- Moving scheduling outside the app process
