# Python Project 50

[![CI Status](https://github.com/skaym00t/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/skaym00t/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d50f2fac7a7c884e161a/maintainability)](https://codeclimate.com/github/skaym00t/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d50f2fac7a7c884e161a/test_coverage)](https://codeclimate.com/github/skaym00t/python-project-50/test_coverage)


### Hexlet tests and linter status:
[![Actions Status](https://github.com/skaym00t/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/skaym00t/python-project-50/actions)

[![Gendiff presentation](https://asciinema.org/a/vq0mvfZidvpnYilAxP0epQzXs.svg)](https://asciinema.org/a/vq0mvfZidvpnYilAxP0epQzXs)

# Gendiff Project

This project provides functionality to generate differences between two JSON files.

## Installation

To set up the project using UV, follow these steps:

1. **Install UV**:
   If you haven't installed UV yet, you can do so by running the following command:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh

2. **Sync dependencies**:
Once UV is installed, navigate to your project directory and sync the dependencies:
bash:
    uv sync

3. **Testing**:
To run tests, use:
bash:
    make test

4. **Example Usage**
Comparing JSON Files:

uv run gendiff examples/file1.json examples/file2.json

Comparing YAML Files:

uv run gendiff examples/file1.yml examples/file2.yml

To run the linter, use:
bash:
    make lint

To run tests with coverage, use:
bash:
    make test-coverage
