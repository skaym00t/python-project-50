install:
	uv sync

run -h:
	uv run gendiff -h

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check --fix .

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build