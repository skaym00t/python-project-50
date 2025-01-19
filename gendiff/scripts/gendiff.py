# python-project-50/gendiff/scripts/gendiff.py
import os

from gendiff.gen_diff import generate_diff
from gendiff.parser import parse_args


def main():
    args = parse_args()
    path1 = os.path.abspath(args.first_file)
    path2 = os.path.abspath(args.second_file)

    format_type = args.format
    print(generate_diff(path1, path2, format_type))


if __name__ == "__main__":
    main()
