from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_json():
    file1_path = './tests/fixtures/file1.json'
    file2_path = './tests/fixtures/file2.json'
    result_path = './tests/fixtures/result_plain_files.txt'
    assert generate_diff(file1_path, file2_path) == open(result_path, 'r').read()


def test_generate_diff_yaml():
    file1_path = './tests/fixtures/file1.yaml'
    file2_path = './tests/fixtures/file2.yaml'
    result_path = './tests/fixtures/result_plain_files.txt'
    assert generate_diff(file1_path, file2_path) == open(result_path, 'r').read()
