import json
import yaml
from yaml.loader import SafeLoader


def parsing_files(first_file, second_file):

    def parse_file(file):
        if file[-4:] == 'json':
            return json.load(open(file))
        elif first_file[-4:] == 'yaml' or first_file[-4:] == '.yml':
            return yaml.load(open(file, 'r'), Loader=SafeLoader)

    return (parse_file(first_file), parse_file(second_file))
