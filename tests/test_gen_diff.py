# python-project-50/tests/test_gen_diff.py
from gendiff.gen_diff import generate_diff

# Тесты для работы с файлами
def test_generate_diff_flat_files():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"
    expected_result = """{
  - a: value1
  + a: new_value1
    b: value2
  + c: value3
}"""
    assert generate_diff(file1_path, file2_path) == expected_result.lower()


def test_generate_diff_flat_yaml_files():
    file1_path = "tests/test_data/file1.yml"
    file2_path = "tests/test_data/file2.yml"
    expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff(file1_path, file2_path).replace("true", "true")
    assert result == expected_result.lower()


# Дополнительные тесты для проверки различных случаев
def test_generate_diff_only_in_file1():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file1.json"
    expected_result = """{
    a: value1
    b: value2
}"""
    # В этом тесте мы используем один и тот же файл для обоих аргументов,
    # чтобы проверить, что функция корректно обрабатывает одинаковые файлы.
    result = generate_diff(file1_path, file2_path)
    assert result == expected_result.lower()


def test_generate_diff_only_in_file2():
    file1_path = "tests/test_data/file2.json"
    file2_path = "tests/test_data/file2.json"
    expected_result = """{
    a: new_value1
    b: value2
    c: value3
}"""
    # В этом тесте мы также используем один и тот же файл для обоих аргументов.
    result = generate_diff(file1_path, file2_path)
    assert result == expected_result.lower()


def test_generate_diff_common_keys_different_values():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"
    expected_result = """{
  - a: value1
  + a: new_value1
    b: value2
  + c: value3
}"""
    result = generate_diff(file1_path, file2_path)
    assert result == expected_result.lower()


def test_generate_diff_common_keys_same_values():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file1.json"
    expected_result = """{
    a: value1
    b: value2
}"""
    result = generate_diff(file1_path, file2_path)
    assert result == expected_result.lower()


def test_generate_diff_mixed_keys():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"
    expected_result = """{
  - a: value1
  + a: new_value1
    b: value2
  + c: value3
}"""
    result = generate_diff(file1_path, file2_path)
    assert result == expected_result.lower()
