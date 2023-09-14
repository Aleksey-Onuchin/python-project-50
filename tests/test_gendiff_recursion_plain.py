from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_recursion_plain_json():
    file1_path = './tests/fixtures/file2-1.json'
    file2_path = './tests/fixtures/file2-2.json'
    result_path = './tests/fixtures/result_recursion_plain.txt'
    assert generate_diff(file1_path, file2_path, 'plain') == open(result_path, 'r').read()


def test_generate_diff_recursion_plain_yaml():
    file1_path = './tests/fixtures/file2-1.yaml'
    file2_path = './tests/fixtures/file2-2.yaml'
    result_path = './tests/fixtures/result_recursion_plain.txt'
    assert generate_diff(file1_path, file2_path, 'plain') == open(result_path, 'r').read()