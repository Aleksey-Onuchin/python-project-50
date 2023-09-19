from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_flat_json():
    file1_path = './tests/fixtures/file_flat1.json'
    file2_path = './tests/fixtures/file_flat2.json'
    result_path = './tests/fixtures/result_flat.txt'
    assert generate_diff(file1_path, file2_path, 'stylish') == open(result_path, 'r').read()


def test_generate_diff_flat_yaml():
    file1_path = './tests/fixtures/file_flat1.yaml'
    file2_path = './tests/fixtures/file_flat2.yaml'
    result_path = './tests/fixtures/result_flat.txt'
    assert generate_diff(file1_path, file2_path, 'stylish') == open(result_path, 'r').read()