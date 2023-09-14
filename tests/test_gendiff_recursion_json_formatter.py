from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_recursion_json_formatter_json():
    file1_path = './tests/fixtures/file2-1.json'
    file2_path = './tests/fixtures/file2-2.json'
    result_path = './tests/fixtures/result_recursion_json_formatter.txt'
    assert generate_diff(file1_path, file2_path, 'json_formatter') == open(result_path, 'r').read()


def test_generate_diff_recursion_json_formatter_yaml():
    file1_path = './tests/fixtures/file2-1.yaml'
    file2_path = './tests/fixtures/file2-2.yaml'
    result_path = './tests/fixtures/result_recursion_json_formatter.txt'
    assert generate_diff(file1_path, file2_path, 'json_formatter') == open(result_path, 'r').read()