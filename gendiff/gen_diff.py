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
