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
    assert result == expected_result.lower()


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
    result = generate_diff(file1_path, file2_path, format_name='plain')
    assert result == expected_result.lower()


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
    result = generate_diff(file1_path, file2_path, format_name='plain')
    assert result == expected_result.lower()