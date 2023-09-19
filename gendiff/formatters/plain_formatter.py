def fixing_values(value):
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    else:
        return value if type(value) is int else f"'{value}'"


def plain(keys_list, diff):
    result = ''

    def walk(keys_list, diff, parents, marker):
        nonlocal result
        keys_list = list(keys_list)
        keys_list.sort()
        for key in keys_list:
            temp_list = []
            for elem in diff:
                if elem['key'] == key and elem['parents'] == parents:
                    temp_list.append(elem)
                    if (elem['status'] == 'stay'
                            or elem['status'] == 'modified')\
                            and elem['type'] == 'dict':
                        walk(elem['children'],
                             diff, parents + '.' + elem['key'], '')
            if len(temp_list) == 1:
                if temp_list[0]['status'] == 'added':
                    if temp_list[0]['type'] == 'dict':
                        result += (f"Property '"
                                   f"{(temp_list[0]['parents'] + '.' + temp_list[0]['key'])[1:]}" # noqa
                                   f"' was added with value: [complex value]\n")
                    else:
                        result += (f"Property '"
                                   f"{(temp_list[0]['parents'] + '.' + temp_list[0]['key'])[1:]}" # noqa
                                   f"' was added with value: {fixing_values(temp_list[0]['value'])}\n") # noqa
                if temp_list[0]['status'] == 'removed':
                    result += (f"Property '"
                               f"{(temp_list[0]['parents'] + '.' + temp_list[0]['key'])[1:]}" # noqa
                               f"' was removed\n")
            else:
                for element in temp_list:
                    if element['status'] == 'removed':
                        value1 = '[complex value]'\
                            if element['type'] == 'dict'\
                            else fixing_values(element['value'])
                    elif element['status'] == 'added':
                        value2 = '[complex value]'\
                            if element['type'] == 'dict'\
                            else fixing_values(element['value'])
                result += (f"Property '"
                           f"{(temp_list[0]['parents'] + '.' + temp_list[0]['key'])[1:]}" # noqa
                           f"' was updated. From {value1} to {value2}\n")
        return result.rstrip()
    return walk(keys_list, diff, '', '')
