#!/usr/bin/env python3
import argparse
import json
import os

parser = argparse.ArgumentParser(
    prog="gendiff", usage="Compares two configuration files and shows a difference."
)
parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format of output")

args = parser.parse_args()

path1 = os.path.abspath(args.first_file)
path2 = os.path.abspath(args.second_file)

file1 = json.load(open(path1))
file2 = json.load(open(path2))


def generate_diff(file1, file2):
    keys = sorted(set(file1.keys()) | set(file2.keys()))
    result = ""
    for key in keys:
        if key in file1 and key not in file2:
            result += f"- {key}: {file1[key]}\n"
        elif key in file2 and key not in file1:
            result += f"+ {key}: {file2[key]}\n"
        elif key in file1 and key in file2:
            if file1[key] != file2[key]:
                result += f"- {key}: {file1[key]}\n"
                result += f"+ {key}: {file2[key]}\n"
            else:
                result += f"  {key}: {file1[key]}\n"
    return result.lower()
