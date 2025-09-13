# Image coordinates (override via env or make vars)
IMAGE_NAME ?= weekly-gen
IMAGE_TAG  ?= latest

.PHONY: build push up down logs run

build:
	IMAGE_NAME=$(IMAGE_NAME) IMAGE_TAG=$(IMAGE_TAG) docker compose build

push:
	IMAGE_NAME=$(IMAGE_NAME) IMAGE_TAG=$(IMAGE_TAG) docker compose push

up:
	IMAGE_NAME=$(IMAGE_NAME) IMAGE_TAG=$(IMAGE_TAG) docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f

run:
	IMAGE_NAME=$(IMAGE_NAME) IMAGE_TAG=$(IMAGE_TAG) docker compose run --rm weekly-gen

