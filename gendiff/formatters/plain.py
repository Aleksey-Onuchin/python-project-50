def fixing_values(value):
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    else:
        return f"'{value}'"


def plain(keys_list, diff):
    result = ''

    def walk(keys_list, diff, parent, marker):
        nonlocal result
        keys_list = list(keys_list)
        keys_list.sort()
        for key in keys_list:
            diff_temp = []
            for elem in diff:
                if elem['key'] == key:
                    diff_temp.append(elem)
                    if elem['status'] == 'stay' and elem['type'] == 'dict':
                        walk(elem['value'], diff, parent +
                             '.' + elem['key'], '')
            if len(diff_temp) == 1:
                if diff_temp[0]['status'] == 'added':
                    if diff_temp[0]['type'] == 'dict':
                        result += (f"Property "
                                   f"'{(diff_temp[0]['parent'] + '.' + diff_temp[0]['key'])[1:]}'" # noqa
                                   f" was added with value: [complex value]\n")
                    else:
                        result += (f"Property "
                                   f"'{(diff_temp[0]['parent'] + '.' + diff_temp[0]['key'])[1:]}'" # noqa
                                   f" was added with value: "
                                   f"{fixing_values(diff_temp[0]['value'])}\n")
                if diff_temp[0]['status'] == 'removed':
                    result += (f"Property "
                               f"'{(diff_temp[0]['parent'] + '.' + diff_temp[0]['key'])[1:]}'" # noqa
                               f" was removed\n")
            else:
                value1 = '[complex value]' \
                    if diff_temp[0]['type'] == 'dict' \
                    else fixing_values(diff_temp[0]['value'])
                value2 = '[complex value]' \
                    if diff_temp[1]['type'] == 'dict' \
                    else fixing_values(diff_temp[1]['value'])
                result += (f"Property "
                           f"'{(diff_temp[0]['parent'] + '.' + diff_temp[0]['key'])[1:]}'" # noqa
                           f" was updated. From {value1} to {value2}\n")
        return result.rstrip()

    return walk(keys_list, diff, '', '')
