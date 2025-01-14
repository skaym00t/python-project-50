install:
	uv sync

run:
	uv run gendiff -h

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check --fix .

check: lint test

build:
	uv build

.PHONY: install test lint check build