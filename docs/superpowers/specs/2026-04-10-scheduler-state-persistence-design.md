# Scheduler State Persistence Design

## Goal

Persist the scheduler's latest execution state and next scheduled run time to a local JSON file so the service can still report the previous execution status after a restart, without introducing a database.

## Current State

- The scheduler keeps runtime state only in memory via `RunState`.
- `/status` returns that in-memory state.
- The scraper already persists issue de-duplication state to `last_run_info.json`.
- The container already bind-mounts `./outputs` to `/app/outputs`, so files under `outputs/` persist on the host.

## Requirements

- Persist only the latest scheduler state, not full history.
- Reuse the existing `/status` response shape.
- Store the persisted file in a host-mounted path.
- Avoid introducing a database or external service.
- Preserve the current daily `09:00` scheduling behavior.

## Options Considered

### Option A: Persist the latest scheduler state to a single JSON file

Use a file such as `outputs/service_state.json` to store the latest scheduler state.

Pros:
- Minimal complexity
- Matches the project's existing JSON-file persistence style
- Sufficient for restart visibility

Cons:
- No historical run timeline

### Option B: Persist a rolling history in JSON

Store the latest state plus the last N runs.

Pros:
- Better debugging context

Cons:
- More file structure and retention logic
- Not needed for the current request

### Option C: Persist via SQLite

Use a small embedded database for scheduler state.

Pros:
- More robust for future expansion

Cons:
- Introduces database design where the project currently has none
- Overkill for the current requirement

## Decision

Use Option A.

The requirement is specifically to remember the previous execution status after a restart. A single JSON state file is the simplest solution that satisfies that without changing the project's architecture.

## Proposed Design

### State File Location

Persist the scheduler state to:

- `outputs/service_state.json`

Because `outputs/` is already bind-mounted to the host, the file will survive container recreation and remain visible on the local machine.

### Persisted Fields

Persist exactly these fields from `RunState`:

- `running`
- `last_started_at`
- `last_finished_at`
- `last_returncode`
- `last_duration_sec`
- `last_log_file`
- `schedule_mode`
- `schedule_time`
- `schedule_timezone`
- `next_scheduled_at`

### Read/Write Lifecycle

- On scheduler initialization:
  - Attempt to load `outputs/service_state.json`
  - Merge valid persisted values into the in-memory `RunState`
  - Recompute `next_scheduled_at` from current time and schedule config to avoid stale future timestamps
- On `run_once()` start:
  - Update in-memory state
  - Persist immediately
- On `run_once()` finish:
  - Update in-memory state
  - Persist again
- Whenever daily scheduling refreshes `next_scheduled_at`:
  - Persist the new value

### Failure Semantics

This design preserves scheduler visibility, not job compensation.

That means:
- After restart, `/status` can still show the previous execution information
- If the service was down during `09:00`, it will not backfill the missed run
- The next scheduled run will be recomputed from current time

### Error Handling

- If `service_state.json` does not exist, start with defaults
- If the file exists but cannot be parsed, ignore it and continue with defaults
- If persistence fails during runtime, append an error to `outputs/service_logs/scheduler-errors.log` but do not crash the service

### API Behavior

No API schema change is required.

`GET /status` will continue returning the same fields, but those fields will now survive service restarts.

## Files Expected To Change

- `app/scheduler.py`
- `tests/test_scheduler.py`
- `README.md`

## Verification Plan

1. Add tests for state-file load and save behavior.
2. Run unit tests.
3. Rebuild and restart the container.
4. Trigger `POST /run-now`.
5. Confirm `outputs/service_state.json` exists on the host.
6. Restart the service.
7. Confirm `GET /status` still shows the last execution information.

## Non-Goals

- Persisting a multi-run execution history
- Backfilling missed runs
- Adding a database
