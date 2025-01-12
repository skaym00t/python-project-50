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

check: test lint

build:
	uv build

reinstall: install build
	uv tool install --reinstall  dist/hexlet_code-0.1.0-py3-none-any.whl

.PHONY: install test lint selfcheck check build reinstall