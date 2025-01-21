# python-project-50/gendiff/formatters/stylish.py

def format_stylish(diff, indent=0):
    lines = []
    spaces_count = 4
    for node in diff:
        if node["type"] == "added":
            lines.append(
                f"{' ' * indent}+ {node['key']}: "
                f"{format_value(node['value'], indent + spaces_count)}"
            )
        elif node["type"] == "removed":
            lines.append(
                f"{' ' * indent}- {node['key']}: "
                f"{format_value(node['value'], indent + spaces_count)}"
            )
        elif node["type"] == "changed":
            lines.append(
                f"{' ' * indent}- {node['key']}: "
                f"{format_value(node['old_value'], indent + spaces_count)}"
            )
            lines.append(
                f"{' ' * indent}+ {node['key']}: "
                f"{format_value(node['new_value'], indent + spaces_count)}"
            )
        elif node["type"] == "unchanged":
            lines.append(
                f"{' ' * indent}  {node['key']}: "
                f"{format_value(node['value'], indent + spaces_count)}"
            )
        elif node["type"] == "nested":
            lines.append(f"{' ' * indent}  {node['key']}: {{")
            lines.append(
                format_stylish(node["children"], indent + spaces_count)
            )
            lines.append(f"{' ' * indent}  }}")
    return "\n".join(lines)

def format_value(value, indent):
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(
                f"{' ' * (indent + 2)}{k}: " f"{format_value(v, indent + 2)}"
            )
        return "{\n" + "\n".join(lines) + "\n" + " " * indent + "}"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)