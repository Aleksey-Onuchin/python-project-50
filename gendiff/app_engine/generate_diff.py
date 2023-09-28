from gendiff.app_engine.parsing_module import parsing_files
from gendiff.app_engine.make_diff import make_diff
from gendiff.app_engine.formatter_processing import formatter_processing


def generate_diff(first_file, second_file, formatter='stylish'):
    dict_file1 = parsing_files(open(first_file), (first_file.split('.'))[-1])
    dict_file2 = parsing_files(open(second_file), (second_file.split('.'))[-1])
    diff = make_diff(dict_file1, dict_file2)
    return formatter_processing(diff, dict_file1, dict_file2, formatter)
