import itertools


def fixing_values(value):
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    else:
        return value


def stylish(keys, diff):

    def walk(children, parents, value, marked_by):
        if children == '':
            return f"{fixing_values(value)}"
        else:
            children.sort()
            lines = []
            for key in children:
                for elem in diff:
                    if elem['key'] == key and elem['parents'] == parents:
                        if marked_by != '':
                            indent = f"{(elem['depth'] * 4) * ' '}"
                        elif elem['status'] == 'removed':
                            indent = f"{(elem['depth'] * 4 - 2) * ' '}- "
                        elif elem['status'] == 'added':
                            indent = f"{(elem['depth'] * 4 - 2) * ' '}+ "
                        else:
                            indent = f"{(elem['depth'] * 4) * ' '}"
                        if elem['type'] == 'dict' \
                                and (elem['status'] == 'added'
                                     or elem['status'] == 'removed') \
                                and marked_by == '':
                            marked_by = elem['key']
                        lines.append(f"{indent}{elem['key']}: {walk(elem['children'], elem['parents'] + '.' + elem['key'], elem['value'], marked_by)}") # noqa
                        if marked_by == elem['key']:
                            marked_by = ''
                        result = itertools.chain(
                            '{', lines, [(elem['depth'] - 1) * 4 * ' ' + '}'])
            return '\n'.join(result)
    return walk(keys, '', '', '')
