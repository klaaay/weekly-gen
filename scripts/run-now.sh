#!/usr/bin/env bash
set -euo pipefail

# Trigger an immediate background run via FastAPI endpoint.
# Config:
#   BASE_URL: service base URL (default: http://localhost:8111)

BASE_URL=${BASE_URL:-http://localhost:8111}

echo "[run-now] POST ${BASE_URL}/run-now"

tmp_resp=$(mktemp)
trap 'rm -f "$tmp_resp"' EXIT

# Perform request and capture HTTP status code
set +e
code=$(curl -sS -o "$tmp_resp" -w "%{http_code}" \
  -X POST "${BASE_URL}/run-now" \
  -H 'Content-Type: application/json' \
  -d '{}' )
curl_rc=$?
set -e

if [ "$curl_rc" -ne 0 ]; then
  echo "[run-now] curl error (rc=$curl_rc)"
  cat "$tmp_resp" || true
  exit "$curl_rc"
fi

echo "[run-now] HTTP $code"
cat "$tmp_resp"
echo

if [ "$code" = "409" ]; then
  echo "[run-now] Job already running (HTTP 409)."
  exit 0
fi

if [ "$code" -lt 200 ] || [ "$code" -ge 300 ]; then
  echo "[run-now] Request failed." >&2
  exit 1
fi

echo "[run-now] Triggered successfully."

