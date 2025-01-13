from gendiff.gen_diff import generate_diff


def test_generate_diff():
    file1 = {"a": 1, "b": 2}
    file2 = {"a": 1, "b": 2}
    expected_output = "  a: 1\n  b: 2\n"
    assert generate_diff(file1, file2) == expected_output.lower()


test_generate_diff()
