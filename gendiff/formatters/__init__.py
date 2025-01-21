# python-project-50/gendiff/formatters/__init__.py
from .json import format_json
from .plain import format_plain
from .stylish import format_stylish

__all__ = ["format_plain", "format_stylish", "format_json"]
