import json


def format_json(diff):
    def format_node(node):
        if node["type"] == "added":
            return {"type": "added", "value": node["value"]}
        elif node["type"] == "removed":
            return {"type": "removed", "value": node["value"]}
        elif node["type"] == "changed":
            return {
                "type": "changed",
                "old_value": node["old_value"],
                "new_value": node["new_value"],
            }
        elif node["type"] == "unchanged":
            return {"type": "unchanged", "value": node["value"]}
        elif node["type"] == "nested":
            children = {
                child["key"]: format_node(child) for child in node["children"]
                }
            return children

    diff_dict = {node["key"]: format_node(node) for node in diff}
    return json.dumps(diff_dict, indent=2)
