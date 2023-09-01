import json
import yaml
from yaml.loader import SafeLoader


def parsing_files(first_file, second_file):
    if first_file[-4:] == 'json':
        file1 = json.load(open(first_file))
        file2 = json.load(open(second_file))
    if first_file[-4:] == 'yaml' or first_file[-4:] == '.yml':
        f1 = open(first_file, 'r')
        f2 = open(second_file, 'r')
        file1 = yaml.load(f1, Loader=SafeLoader)
        file2 = yaml.load(f2, Loader=SafeLoader)
    keys = sorted(set(file1.keys() | set(file2.keys())))
    return (file1, file2, keys)
