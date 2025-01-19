# python-project-50/gendiff/gen_diff.py
import json
import os

import yaml

from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def parse_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    with open(file_path, "r") as f:
        if file_extension in [".yaml", ".yml"]:
            return yaml.safe_load(f)
        elif file_extension == ".json":
            return json.load(f)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []
    for key in keys:
        if key not in data1:
            diff.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })
        elif key not in data2:
            diff.append({
                'key': key,
                'type': 'removed',
                'value': data1[key]
            })
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                nested_diff = build_diff(data1[key], data2[key])
                if nested_diff:
                    diff.append({
                        'key': key,
                        'type': 'nested',
                        'children': nested_diff
                    })
            elif data1[key] != data2[key]:
                diff.append({
                    'key': key,
                    'type': 'changed',
                    'old_value': data1[key],
                    'new_value': data2[key]
                })
            else:
                diff.append({
                    'key': key,
                    'type': 'unchanged',
                    'value': data1[key]
                })
    return diff


def generate_diff(file1_path, file2_path, format_name='stylish'):
    file1 = parse_file(file1_path)
    file2 = parse_file(file2_path)
    diff = build_diff(file1, file2)
    
    if format_name == 'stylish':
        result = "{\n" + format_stylish(diff, indent=2) + "\n}"
        return result.lower()
    elif format_name == 'plain':
        result = format_plain(diff)
        return result.lower()
    # Можно добавить другие форматеры позже
    raise ValueError(f"Unsupported format: {format_name}")