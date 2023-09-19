def fixing_values(value):
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    else:
        return value


def stylish(keys_list, diff):
    result = ''

    def walk(keys_list, diff, parents, marker):
        nonlocal result
        keys_list = list(keys_list)
        keys_list.sort()
        for key in keys_list:
            for elem in diff:
                if elem['key'] == key:
                    if (elem['status'] == 'stay'
                            or elem['status'] == 'modified')\
                            and elem['type'] == 'dict'\
                            and elem['parents'] == parents:
                        result += (f"{int(elem['depth']) * 4 * ' '}"
                                   f"{elem['key']}: {{\n")
                        walk(elem['children'], diff,
                             parents + '.' + elem['key'], '')
                        result += f"{int(elem['depth']) * 4 * ' '}}}\n"
                    elif elem['status'] == 'stay'\
                            and elem['type'] == 'value'\
                            and elem['parents'] == parents:
                        result += (f"{int(elem['depth']) * 4 * ' '}"
                                   f"{elem['key']}: "
                                   f"{fixing_values(elem['value'])}\n")
                    elif elem['status'] == 'removed'\
                            and elem['type'] == 'dict'\
                            and elem['parents'] == parents:
                        if elem['parents'] == parents:
                            if marker == 'no':
                                result += (f"{((int(elem['depth']) * 4) * ' ')}"
                                           f"{elem['key']}: {{\n")
                                walk(elem['children'], diff,
                                     parents + '.' + elem['key'], 'no')
                                result += f"{int(elem['depth']) * 4 * ' '}}}\n"
                            else:
                                result += (f"{(((int(elem['depth']) * 4) -2) * ' ')}" # noqa
                                           f"- {elem['key']}: {{\n")
                                walk(elem['children'], diff,
                                     parents + '.' + elem['key'], 'no')
                                result += f"{int(elem['depth']) * 4 * ' '}}}\n"
                        else:
                            pass
                    elif elem['status'] == 'removed'\
                            and elem['parents'] == parents:
                        if elem['parents'] == parents:
                            if marker == 'no':
                                result += (f"{((int(elem['depth']) * 4) * ' ')}"
                                           f"{elem['key']}: "
                                           f"{fixing_values(elem['value'])}\n")
                            else:
                                result += (f"{(((int(elem['depth']) * 4) -2) * ' ')}" # noqa
                                           f"- {elem['key']}: "
                                           f"{fixing_values(elem['value'])}\n")
                        else:
                            pass
                    elif elem['status'] == 'added'\
                            and elem['type'] == 'dict'\
                            and elem['parents'] == parents:
                        if elem['parents'] == parents:
                            if marker == 'no':
                                result += (f"{((int(elem['depth']) * 4) * ' ')}"
                                           f"{elem['key']}: {{\n")
                                walk(elem['children'], diff,
                                     parents + '.' + elem['key'], 'no')
                                result += f"{int(elem['depth']) * 4 * ' '}}}\n"
                            else:
                                result += (f"{(((int(elem['depth']) * 4) -2) * ' ')}" # noqa
                                           f"+ {elem['key']}: {{\n")
                                walk(elem['children'], diff,
                                     parents + '.' + elem['key'], 'no')
                                result += f"{int(elem['depth']) * 4 * ' '}}}\n"
                        else:
                            pass
                    elif elem['status'] == 'added'\
                            and elem['parents'] == parents:
                        if elem['parents'] == parents:
                            if marker == 'no':
                                result += (f"{((int(elem['depth']) * 4) * ' ')}"
                                           f"{elem['key']}: "
                                           f"{fixing_values(elem['value'])}\n")
                            else:
                                result += (f"{(((int(elem['depth']) * 4) -2) * ' ')}" # noqa
                                           f"+ {elem['key']}: "
                                           f"{fixing_values(elem['value'])}\n")
                        else:
                            pass
        return f"{{\n{result.rstrip()}\n}}"
    return walk(keys_list, diff, '', '')
