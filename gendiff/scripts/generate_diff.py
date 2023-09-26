from gendiff.scripts.parsing_module import parsing_files
from gendiff.scripts.make_diff import make_diff
from gendiff.scripts.formatter_processing import formatter_processing


def generate_diff(first_file, second_file, formatter='stylish'):
    dict_file1, dict_file2 = parsing_files(first_file, second_file)
    diff = make_diff(dict_file1, dict_file2)
    return formatter_processing(diff, dict_file1, dict_file2, formatter)
