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

    def walk(children, parents):
        nonlocal result
        children.sort()
        for key in children:
            temp_list = []
            for elem in diff:
                if elem['key'] == key and elem['parents'] == parents:
                    temp_list.append(elem)
                    if elem['type'] == 'dict' \
                            and (elem['status'] == 'stay'
                                 or elem['status'] == 'modified'):
                        walk(elem['children'], elem['parents'] + '.' + elem['key']) # noqa
            name = (temp_list[0]['parents'] + '.' + temp_list[0]['key'])[1:]
            if len(temp_list) == 1 and (temp_list[0]['status'] == 'added'
                                        or temp_list[0]['status'] == 'removed'):
                value = fixing_values(
                    temp_list[0]['value']) if temp_list[0]['type'] != 'dict' else '[complex value]' # noqa
                last_part = f" with value: {value}" \
                            if temp_list[0]['status'] == 'added' else ''
                result += f"Property '{name}' was {temp_list[0]['status']}{last_part}\n" # noqa
            elif len(temp_list) == 2:
                elem_from = list(filter(lambda value: value['status'] == 'removed', temp_list)) # noqa
                value_from = fixing_values(elem_from[0]['value']) \
                    if elem_from[0]['type'] != 'dict' \
                    else '[complex value]'
                elem_to = list(filter(lambda value: value['status'] == 'added', temp_list)) # noqa
                value_to = fixing_values(elem_to[0]['value']) \
                    if elem_to[0]['type'] != 'dict' \
                    else '[complex value]'
                result += (f"Property '{name}' was updated. From {value_from} to {value_to}\n") # noqa
        return result.rstrip()
    return walk(keys_list, '')
