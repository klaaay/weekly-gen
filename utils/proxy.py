#!/usr/bin/env python3
"""Proxy helpers to centralize proxy setup for requests.

Priority order for proxy resolution:
1) PROXY_URL env (e.g., http://host:port)
2) HTTP_PROXY/HTTPS_PROXY envs (standard; if both set, keep them)
3) Build from PROXY_HOST/PROXY_PORT/PROXY_SCHEME envs
4) Sensible defaults:
   - Inside container: http://host.docker.internal:7897
   - Outside container: http://127.0.0.1:7897
"""
from __future__ import annotations

import os


def _in_container() -> bool:
    # Docker sets this file in containers; also allow explicit override
    return os.path.exists("/.dockerenv") or os.getenv("RUNNING_IN_CONTAINER") == "1"


def _default_host() -> str:
    # Ensure host is reachable from inside container
    return "host.docker.internal" if _in_container() else "127.0.0.1"


def _normalize_url(url: str | None) -> str | None:
    if not url:
        return None
    if "://" not in url:
        return f"http://{url}"
    return url


def get_proxies() -> dict:
    # Highest priority: explicit PROXY_URL
    proxy_url = _normalize_url(os.getenv("PROXY_URL"))
    if proxy_url:
        return {"http": proxy_url, "https": proxy_url}

    # Next: standard HTTP(S)_PROXY environment variables
    http_env = _normalize_url(os.getenv("HTTP_PROXY") or os.getenv("http_proxy"))
    https_env = _normalize_url(os.getenv("HTTPS_PROXY") or os.getenv("https_proxy"))
    if http_env or https_env:
        # If only one is set, use it for both to keep behavior consistent
        base = https_env or http_env
        return {
            "http": http_env or base,
            "https": https_env or base,
        }

    # Next: compose from PROXY_HOST/PORT/SCHEME
    host = os.getenv("PROXY_HOST") or _default_host()
    port = os.getenv("PROXY_PORT") or "7897"
    scheme = os.getenv("PROXY_SCHEME") or "http"
    url = f"{scheme}://{host}:{port}"
    return {"http": url, "https": url}


def proxy_for_log() -> str:
    p = get_proxies()
    return p.get("http") or p.get("https") or "<none>"

