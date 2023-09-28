from gendiff.app_engine.make_diff import keys
from gendiff.formatters.stylish_formatter import stylish
from gendiff.formatters.plain_formatter import plain
from gendiff.formatters.json_formatter import json_formatter


def formatter_processing(diff, dict_file1, dict_file2, formatter):
    _, first_level_keys = keys(dict_file1, dict_file2)
    if formatter == 'stylish':
        return stylish(first_level_keys, diff)
    elif formatter == 'plain':
        return plain(first_level_keys, diff)
    elif formatter == 'json':
        return json_formatter(diff)
