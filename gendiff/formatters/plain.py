# python-project-50/gendiff/formatters/plain.py
def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return f"'{value}'"


def format_plain(diff, parent_key=''):
    lines = []
    for node in diff:
        key = f"{parent_key}.{node['key']}" if parent_key else node['key']
        if node['type'] == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{key}' was added with value: {value}")
        elif node['type'] == 'removed':
            lines.append(f"Property '{key}' was removed")
        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(
                f"Property '{key}' was updated. From {old_value} to {new_value}"
                )
        elif node['type'] == 'unchanged':
            continue
        elif node['type'] == 'nested':
            lines.append(format_plain(node['children'], key))
    return '\n'.join(lines)