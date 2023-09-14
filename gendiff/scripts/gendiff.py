import argparse
from gendiff.scripts.parsing_module import parsing_files
from gendiff.formatters.stylish_formatter import stylish
from gendiff.formatters.plain_formatter import plain
from gendiff.formatters.json_formatter import json_formatter


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        default='stylish', help='set format of output')
    args = parser.parse_args()
    return generate_diff(args.format, args.first_file, args.second_file)


def prep_diff(dict_file):
    res = []

    def walk(node, depth, parent):
        keys = list(node.keys())
        for key in keys:
            if type(node[key]) is not dict:
                res.append({'key': key, 'depth': depth,
                            'type': 'value', 'value': node[key],
                            'parent': parent})
            else:
                children = list(node[key].keys())
                res.append({'key': key, 'depth': depth,
                            'type': 'dict', 'value': children,
                            'parent': parent})
                walk(node[key], depth + 1, parent + '.' + key)
        return res
    return walk(dict_file, 1, '')


def make_diff(keys_list, file1, file2):
    res = []
    for key in keys_list:
        for elem in file1:
            if elem.get('key') == key:
                test1 = elem
                break
            else:
                test1 = None
        for elem in file2:
            if elem.get('key') == key:
                test2 = elem
                break
            else:
                test2 = None
        if test1 is None and test2 is not None:
            test2['status'] = 'added'
            res.append(test2)
        elif test1 is not None and test2 is None:
            test1['status'] = 'removed'
            res.append(test1)
        elif test1 is not None and \
                test2 is not None and \
                test1['type'] != 'dict' and \
                test2['type'] != 'dict' and \
                test1['value'] != test2['value']:
            test1['status'] = 'removed'
            test2['status'] = 'added'
            res.append(test1)
            res.append(test2)
        elif test1 is not None and \
                test2 is not None and \
                test1['type'] != 'dict' and \
                test2['type'] != 'dict' and \
                test1['value'] == test2['value']:
            if test1['parent'] == test2['parent']:
                test1['status'] = 'stay'
                res.append(test1)
            else:
                test1['status'] = 'removed'
                test2['status'] = 'added'
                res.append(test1)
                res.append(test2)
        elif test1 is not None and \
                test2 is not None and \
                test1['type'] == 'dict' and \
                test2['type'] != 'dict':
            test1['status'] = 'removed'
            test2['status'] = 'added'
            res.append(test1)
            res.append(test2)
        elif test1 is not None and \
                test2 is not None and \
                test1['type'] != 'dict' and \
                test2['type'] == 'dict':
            test1['status'] = 'removed'
            test2['status'] = 'added'
            res.append(test1)
            res.append(test2)
        elif test1 is not None and \
                test2 is not None and \
                test1['type'] == 'dict' and \
                test2['type'] == 'dict':
            if test1['parent'] == test2['parent']:
                test1['status'] = 'stay'
                test1['value'] = (set(test1['value']) | set(test2['value']))
                res.append(test1)
            else:
                test1['status'] = 'removed'
                test2['status'] = 'added'
                res.append(test1)
                res.append(test2)
    return res


def list_of_keys(diff_from_file):
    list = []
    for elem in diff_from_file:
        list.append(elem['key'])
    return list


def general_list_of_keys(file1, file2):
    diff_from_file1 = prep_diff(file1)
    diff_from_file2 = prep_diff(file2)
    general_keys_list = set(list_of_keys(diff_from_file1)) | set(
        list_of_keys(diff_from_file2))
    return general_keys_list


def first_level_keys(diff_from_file):
    first_level = []
    for key in diff_from_file:
        if key['depth'] == 1:
            first_level.append(key['key'])
    return first_level


def general_first_level_keys(file1, file2):
    diff_from_file1 = prep_diff(file1)
    diff_from_file2 = prep_diff(file2)
    first_level_keys_list = set(first_level_keys(diff_from_file1)) | set(
        first_level_keys(diff_from_file2))
    return first_level_keys_list


def generate_diff(formatter, first_file, second_file):
    dict_file1, dict_file2 = parsing_files(first_file, second_file)
    general_keys_list = general_list_of_keys(dict_file1, dict_file2)
    first_level_keys_list = general_first_level_keys(dict_file1, dict_file2)
    diff = make_diff(general_keys_list, prep_diff(dict_file1), prep_diff(dict_file2)) # noqa
    if formatter == 'stylish':
        return stylish(first_level_keys_list, diff)
    elif formatter == 'plain':
        return plain(first_level_keys_list, diff)
    elif formatter == 'json_formatter':
        return json_formatter(diff)


if __name__ == '__main__':
    main()
