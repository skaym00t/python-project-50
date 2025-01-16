# python-project-50/gendiff/gen_diff.py
import json
import yaml
import os


def parse_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    with open(file_path, "r") as f:
        if file_extension in [".yaml", ".yml"]:
            return yaml.safe_load(f)
        elif file_extension == ".json":
            return json.load(f)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")


def generate_diff(file1_path, file2_path):
    file1 = parse_file(file1_path)
    file2 = parse_file(file2_path)

    keys = sorted(set(file1.keys()) | set(file2.keys()))
    result = "{\n"
    for key in keys:
        if key in file1 and key not in file2:
            result += f"  - {key}: {file1[key]}\n"
        elif key in file2 and key not in file1:
            result += f"  + {key}: {file2[key]}\n"
        elif key in file1 and key in file2:
            if file1[key] != file2[key]:
                result += f"  - {key}: {file1[key]}\n"
                result += f"  + {key}: {file2[key]}\n"
            else:
                result += f"    {key}: {file1[key]}\n"
    result += "}"
    return result.lower()
