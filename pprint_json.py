import json
from sys import argv


def load_json_input(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        json_input = json.load(f)
    return json_input


def pretty_print_json(json_input):
    pretty_json = json.dumps(json_input, sort_keys=True, indent=4, ensure_ascii=False)
    return pretty_json


def main():
    try:
        json_input = load_json_input(argv[1])
        print(pretty_print_json(json_input))
    except IndexError:
        print('Invalid filepath')
    except FileNotFoundError:
        print('File not found')
    except json.JSONDecodeError as err:
        print('Bad json: {}'.format(err))
    pass


if __name__ == '__main__':
    main()
