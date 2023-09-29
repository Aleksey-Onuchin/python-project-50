from gendiff.get_arguments import get_arguments
from gendiff.generate_diff import generate_diff


def main():
    first_file, second_file, formatter = get_arguments()
    print(generate_diff(first_file, second_file, formatter))


if __name__ == '__main__':
    main()
