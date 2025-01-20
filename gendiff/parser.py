# python-project-50/gendiff/parser.py
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", help="Path to the first file")
    parser.add_argument("second_file", help="Path to the second file")
    parser.add_argument(
        "-f",
        "--format",
        choices=["stylish", "plain", "json"],
        default="stylish",
        help="set format of output (default: stylish)",
    )
    return parser.parse_args()
