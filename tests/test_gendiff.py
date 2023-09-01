from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_json():
    file1_path = './tests/fixtures/file1.json'
    file2_path = './tests/fixtures/file2.json'
    result_path = 'fixtures/result.txt'

    assert generate_diff(
        file1_path, file2_path) == "- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true"


def test_generate_diff_yaml():
    file1_path = './tests/fixtures/file1.yaml'
    file2_path = './tests/fixtures/file2.yaml'
    result_path = 'fixtures/result.txt'

    assert generate_diff(
        file1_path, file2_path) == "- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true"
