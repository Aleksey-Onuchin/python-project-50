import json


def json_formatter(diff):
    result = ''
    keys = []
    for elem in diff:
        keys.append(elem['key'])
    unic_keys = list(set(keys))
    unic_keys.sort()
    for key in unic_keys:
        for elem in diff:
            if key == elem['key']:
                temp_dict = {}
                for k, v in elem.items():
                    if type(v) is set or type(v) is list:
                        v1 = list(v)
                        v1.sort()
                    else:
                        v1 = v
                    temp_dict[k] = v1
                result += f"{json.dumps(temp_dict)}\n"
    return str(result.rstrip())
