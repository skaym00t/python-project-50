# python-project-50/tests/test_gen_diff.py
from gendiff.gen_diff import generate_diff


def test_generate_diff_flat_files():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"
    expected_result = """{
    common: {
      + follow: false
        setting1: value 1
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
    print("Generated diff:")
    print(result)
    print("Expected diff:")
    print(expected_result.lower())
    assert result == expected_result.lower()


def test_generate_diff_flat_yaml_files():
    file1_path = "tests/test_data/file1.yml"
    file2_path = "tests/test_data/file2.yml"
    expected_result = """{
    common: {
      + follow: false
        setting1: value 1
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
    print("Generated diff:")
    print(result)
    print("Expected diff:")
    print(expected_result.lower())
    assert result == expected_result.lower()
