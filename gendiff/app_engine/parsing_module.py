import json
import yaml
from yaml.loader import SafeLoader


def parsing_files(opened_file, extension):
    if extension == 'json':
        return json.load(opened_file)
    elif extension == 'yaml' or extension == 'yml':
        return yaml.load(opened_file, Loader=SafeLoader)
