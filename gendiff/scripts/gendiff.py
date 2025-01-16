# python-project-50/gendiff/scripts/gendiff.py
import os
from gendiff import generate_diff, parse_args


def main():
    args = parse_args()
    path1 = os.path.abspath(args.first_file)
    path2 = os.path.abspath(args.second_file)
    print(generate_diff(path1, path2))


if __name__ == "__main__":
    main()
