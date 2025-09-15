# syntax=docker/dockerfile:1

# Use uv's official image with Python preinstalled
FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /app

# Set timezone to UTC+8 (Asia/Shanghai)
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai
RUN apt-get update \
    && apt-get install -y --no-install-recommends tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies first (with caching) using uv
COPY pyproject.toml ./
RUN uv sync --frozen || uv sync

# Copy the project
COPY . .

# Ensure the venv is used by default
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    WORKDIR=/app \
    RUNNING_IN_CONTAINER=1

EXPOSE 8000

# Run the FastAPI app via uv + uvicorn
CMD ["uv", "run", "uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
