import itertools


def prepare_file_for_diff(dict_file):
    result = []

    def walk(keys, dict_file, depth, parents):
        for key in keys:
            if type(dict_file[key]) is dict:
                result.append({'key': key, 'type': 'dict', 'depth': depth,
                               'parents': parents, 'value': '',
                               'children': list(dict_file[key].keys())})
                walk(list(dict_file[key]), dict_file[key],
                     depth + 1, parents + '.' + key)
            else:
                result.append({'key': key, 'type': 'value', 'depth': depth,
                               'parents': parents, 'value': dict_file[key],
                               'children': ''})
        return result
    return walk(list(dict_file.keys()), dict_file, 1, '')


def keys(*args):
    general_keys = []
    first_level_keys = []

    def make_keys_lists(dict_file):
        for elem in prepare_file_for_diff(dict_file):
            general_keys.append(elem['key'])
            if elem['depth'] == 1:
                first_level_keys.append(elem['key'])
    for dict_file in args:
        make_keys_lists(dict_file)
    return list(set(general_keys)), list(set(first_level_keys))


def make_diff(dict_file1, dict_file2):
    result = []
    file1 = prepare_file_for_diff(dict_file1)
    file2 = prepare_file_for_diff(dict_file2)

    def walk(children, parents):
        children.sort()
        for key in children:
            list1 = list(filter(lambda value: value['key'] == key and value['parents'] == parents, file1)) # noqa
            list2 = list(filter(lambda value: value['key'] == key and value['parents'] == parents, file2)) # noqa
            if list1 == list2:
                list1[0]['status'] = 'stay'
                result.append(list1)
            elif list1 and not list2:
                list1[0]['status'] = 'removed'
                result.append(list1)
            elif not list1 and list2:
                list2[0]['status'] = 'added'
                result.append(list2)
            elif list1[0]['type'] == 'dict' and list2[0]['type'] == 'dict':
                list1[0]['status'] = 'modified'
                children_temp = list1[0]['children'][:]
                children_temp.extend(list2[0]['children'])
                common_children = list(set(children_temp))
                list1[0]['children'] = common_children
                result.append(list1)
            else:
                list1[0]['status'] = 'removed'
                list2[0]['status'] = 'added'
                result.append(list1)
                result.append(list2)
            list_common = list1[:]
            list_common.extend(list2)
            if 'dict' in list(itertools.chain(map(lambda elem: elem['type'], list_common))): # noqa
                children = list(set(itertools.chain(*(map(lambda elem: elem['children'], list_common))))) # noqa
                walk(children, parents + '.' + key)
        return list(itertools.chain(*result))
    return walk((keys(dict_file1, dict_file2))[1], '')
