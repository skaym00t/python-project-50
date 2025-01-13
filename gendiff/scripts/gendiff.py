import json
import os
from gendiff import generate_diff, parse_args

def main():
    args = parse_args()
    path1 = os.path.abspath(args.first_file)
    path2 = os.path.abspath(args.second_file)

    with open(path1) as f1, open(path2) as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)

    print(generate_diff(file1, file2))

if __name__ == "__main__":
    main()