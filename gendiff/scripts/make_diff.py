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


def keys(dict_file1, dict_file2):
    general_keys = []
    first_level_keys = []
    for elem in prepare_file_for_diff(dict_file1):
        general_keys.append(elem['key'])
        if elem['depth'] == 1:
            first_level_keys.append(elem['key'])
    for elem in prepare_file_for_diff(dict_file2):
        general_keys.append(elem['key'])
        if elem['depth'] == 1:
            first_level_keys.append(elem['key'])
    return list(set(general_keys)), list(set(first_level_keys))


def make_diff(dict_file1, dict_file2):
    general_keys, _ = keys(dict_file1, dict_file2)
    general_keys.sort()
    result = []
    for key in general_keys:
        temp_list1 = []
        temp_list2 = []
        for elem1 in prepare_file_for_diff(dict_file1):
            if elem1['key'] == key:
                temp_list1.append(elem1)
        for elem2 in prepare_file_for_diff(dict_file2):
            if elem2['key'] == key:
                temp_list2.append(elem2)
        # print('TL1', temp_list1)
        if temp_list1 and not temp_list2:
            for elem1 in temp_list1:
                elem1['status'] = 'removed'
                if elem1 not in result:
                    result.append(elem1)
        elif not temp_list1 and temp_list2:
            for elem2 in temp_list2:
                elem2['status'] = 'added'
                if elem2 not in result:
                    result.append(elem2)
        for elem1 in temp_list1:
            elem1_temp = dict(elem1)
            for elem2 in temp_list2:
                if elem1 == elem2:
                    elem1_temp['status'] = 'stay'
                    break
                elif elem1['type'] == 'dict' and elem2['type'] == 'dict'\
                        and elem1['parents'] != elem2['parents']:
                    elem1_temp['status'] = 'removed'
                elif elem1['type'] == 'dict' and elem2['type'] == 'dict'\
                        and elem1['parents'] == elem2['parents']:
                    elem1_temp['status'] = 'modified'
                    elem1_temp['children'] = list(
                        set(elem1['children']) | set(elem2['children']))
                elif (elem1['type'] == 'dict'
                      and elem2['type'] != 'dict')\
                    or (elem1['type'] != 'dict'
                        and elem2['type'] == 'dict'):
                    elem1_temp['status'] = 'removed'
                elif elem1['type'] != 'dict'\
                        and elem2['type'] != 'dict'\
                        and (elem1['parents'] != elem2['parents']
                             or elem1['value'] != elem2['value']):
                    elem1_temp['status'] = 'removed'
            if elem1_temp not in result:
                result.append(elem1_temp)
        for elem2 in temp_list2:
            elem2_temp = dict(elem2)
            for elem1 in temp_list1:
                if elem2 == elem1:
                    elem2_temp['status'] = 'stay'
                    break
                elif elem2['type'] == 'dict'\
                        and elem1['type'] == 'dict'\
                        and elem2['parents'] != elem1['parents']:
                    elem2_temp['status'] = 'added'
                elif elem2['type'] == 'dict'\
                        and elem1['type'] == 'dict'\
                        and elem2['parents'] == elem1['parents']:
                    elem2_temp['status'] = 'modified'
                    elem2_temp['children'] = list(
                        set(elem1['children']) | set(elem2['children']))
                elif (elem2['type'] == 'dict'
                        and elem1['type'] != 'dict')\
                        or (elem2['type'] != 'dict'
                            and elem1['type'] == 'dict'):
                    elem2_temp['status'] = 'added'
                elif elem2['type'] != 'dict'\
                        and elem1['type'] != 'dict'\
                        and (elem2['parents'] != elem1['parents']
                             or elem2['value'] != elem1['value']):
                    elem2_temp['status'] = 'added'
            if elem2_temp not in result:
                result.append(elem2_temp)
    return result
