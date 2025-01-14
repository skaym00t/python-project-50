# Python Project 50

[![CI Status](https://github.com/skaym00t/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/skaym00t/python-project-50/actions)
[![Coverage Status](https://api.codeclimate.com/v1/badges/f709be67863098882a771aff05aae9/test_coverage)](https://codeclimate.com/github/skaym00t/python-project-50/test_coverage)


### Hexlet tests and linter status:
[![Actions Status](https://github.com/skaym00t/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/skaym00t/python-project-50/actions)

[![Gendiff presentation](https://asciinema.org/a/4wzy3byzqqrNF7BSIU32xHPka.svg)](https://asciinema.org/a/4wzy3byzqqrNF7BSIU32xHPka)

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

3. **Usage**:
Run the script with two JSON files as arguments:
bash:
    uv run gendiff file1.json(relative path) file2.json(relative path)

4. **Testing**:
To run tests, use:
bash:
    make test

To run the linter, use:
bash:
    make lint

To run tests with coverage, use:
bash:
    make test-coverage
