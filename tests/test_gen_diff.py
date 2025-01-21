# python-project-50/tests/test_gen_diff.py
# tests/test_gen_diff.py
import json
from gendiff.gen_diff import generate_diff

def test_generate_diff_flat_files():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"
    expected_result = """{
        common: {
          + follow: false
            setting1: Value 1
          - setting2: 200
          - setting3: true
          + setting3: null
          + setting4: blah blah
          + setting5: {
                key5: value5
            }
            setting6: {
                doge: {
                  - wow:
                  + wow: so much
                }
                key: value
              + ops: vops
            }
        }
        group1: {
          - baz: bas
          + baz: bars
            foo: bar
          - nest: {
                key: value
            }
          + nest: str
        }
      - group2: {
            abc: 12345
            deep: {
                id: 45
            }
        }
      + group3: {
            deep: {
                id: {
                    number: 45
                }
            }
            fee: 100500
        }
    }"""
    result = generate_diff(file1_path, file2_path)
    assert result == expected_result

def test_generate_diff_flat_yaml_files():
    file1_path = "tests/test_data/file1.yml"
    file2_path = "tests/test_data/file2.yml"
    expected_result = """{
        common: {
          + follow: false
            setting1: Value 1
          - setting2: 200
          - setting3: true
          + setting3: null
          + setting4: blah blah
          + setting5: {
                key5: value5
            }
            setting6: {
                doge: {
                  - wow:
                  + wow: so much
                }
                key: value
              + ops: vops
            }
        }
        group1: {
          - baz: bas
          + baz: bars
            foo: bar
          - nest: {
                key: value
            }
          + nest: str
        }
      - group2: {
            abc: 12345
            deep: {
                id: 45
            }
        }
      + group3: {
            deep: {
                id: {
                    number: 45
                }
            }
            fee: 100500
        }
    }"""
    result = generate_diff(file1_path, file2_path)
    assert result == expected_result

def test_generate_diff_plain_format():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"
    expected_result = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    result = generate_diff(file1_path, file2_path, format_name="plain")
    assert result == expected_result

def test_generate_diff_plain_yaml_format():
    file1_path = "tests/test_data/file1.yml"
    file2_path = "tests/test_data/file2.yml"
    expected_result = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    result = generate_diff(file1_path, file2_path, format_name="plain")
    assert result == expected_result

def test_generate_diff_json_format():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"
    expected_result = """{
  "common": {
    "follow": {"type": "added", "value": false},
    "setting1": {"type": "unchanged", "value": "Value 1"},
    "setting2": {"type": "removed", "value": 200},
    "setting3": {"type": "changed", "old_value": true, "new_value": null},
    "setting4": {"type": "added", "value": "blah blah"},
    "setting5": {"type": "added", "value": {"key5": "value5"}},
    "setting6": {
      "doge": {
        "wow": {"type": "changed", "old_value": "", "new_value": "so much"}
      },
      "key": {"type": "unchanged", "value": "value"},
      "ops": {"type": "added", "value": "vops"}
    }
  },
  "group1": {
    "baz": {"type": "changed", "old_value": "bas", "new_value": "bars"},
    "foo": {"type": "unchanged", "value": "bar"},
    "nest": {
      "type": "changed", "old_value": {"key": "value"}, "new_value": "str"
      }
  },
  "group2": {"type": "removed", "value": {"abc": 12345, "deep": {"id": 45}}},
  "group3": {
    "type": "added", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}
    }
}"""
    result = generate_diff(file1_path, file2_path, format_name="json")
    assert json.loads(result) == json.loads(expected_result)