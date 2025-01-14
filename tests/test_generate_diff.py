import json
from gendiff.gen_diff import generate_diff

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def test_generate_diff_flat_files():
    file1 = load_json('tests/test_data/file1.json')
    file2 = load_json('tests/test_data/file2.json')
    expected_result = "- a: value1\n+ a: new_value1\n  b: value2\n+ c: value3\n"
    assert generate_diff(file1, file2) == expected_result.lower()

def test_generate_diff_only_in_file1():
    file1 = {'a': 'value1', 'b': 'value2'}
    file2 = {}
    expected_result = "- a: value1\n- b: value2\n"
    assert generate_diff(file1, file2) == expected_result

def test_generate_diff_only_in_file2():
    file1 = {}
    file2 = {'a': 'value1', 'b': 'value2'}
    expected_result = "+ a: value1\n+ b: value2\n"
    assert generate_diff(file1, file2) == expected_result

def test_generate_diff_common_keys_different_values():
    file1 = {'a': 'value1', 'b': 'value2'}
    file2 = {'a': 'new_value1', 'b': 'value2'}
    expected_result = "- a: value1\n+ a: new_value1\n  b: value2\n"
    assert generate_diff(file1, file2) == expected_result

def test_generate_diff_common_keys_same_values():
    file1 = {'a': 'value1', 'b': 'value2'}
    file2 = {'a': 'value1', 'b': 'value2'}
    expected_result = "  a: value1\n  b: value2\n"
    assert generate_diff(file1, file2) == expected_result

def test_generate_diff_mixed_keys():
    file1 = {'a': 'value1', 'b': 'value2'}
    file2 = {'b': 'new_value2', 'c': 'value3'}
    expected_result = "- a: value1\n- b: value2\n+ b: new_value2\n+ c: value3\n"
    assert generate_diff(file1, file2) == expected_result