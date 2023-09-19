from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_recursion_stylish_json():
    file1_path = './tests/fixtures/file_test1.json'
    file2_path = './tests/fixtures/file_test2.json'
    result_path = './tests/fixtures/result_recursion_stylish.txt'
    assert generate_diff(file1_path, file2_path, 'stylish') == open(result_path, 'r').read()


def test_generate_diff_recursion_stylish_yaml():
    file1_path = './tests/fixtures/file_test1.yaml'
    file2_path = './tests/fixtures/file_test2.yaml'
    result_path = './tests/fixtures/result_recursion_stylish.txt'
    assert generate_diff(file1_path, file2_path, 'stylish') == open(result_path, 'r').read()