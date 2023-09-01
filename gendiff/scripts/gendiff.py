import argparse
from gendiff.scripts.parsing_module import parsing_files


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        default='', help='set format of output')
    args = parser.parse_args()
    return generate_diff(args.first_file, args.second_file)


def generate_diff(first_file, second_file):
    file1, file2, keys = parsing_files(first_file, second_file)
    result = ''
    for key in keys:
        if file1.get(key) is None:
            result += f"+ {key}: {file2[key]}\n"
        elif file1.get(key) is not None and file2.get(key) is None:
            result += f"- {key}: {file1[key]}\n"
        elif file1.get(key) == file2.get(key):
            result += f"  {key}: {file1[key]}\n"
        else:
            result += f"- {key}: {file1[key]}\n+ {key}: {file2[key]}\n"
    return result.strip().lower()


if __name__ == '__main__':
    main()
