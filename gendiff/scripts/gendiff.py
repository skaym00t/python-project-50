#!/usr/bin/env python3

from gendiff import file1, file2, generate_diff, parser


def main():
    parser.parse_args()
    print(generate_diff(file1, file2))


if __name__ == "__main__":
    main()
