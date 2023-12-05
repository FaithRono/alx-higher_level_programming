#!/usr/bin/python3
import sys
from os import path
from json import dump, load
from importlib.machinery import SourceFileLoader

def load_from_json_file(filename):
    """Loads data from a JSON file."""
    with open(filename, 'r') as file:
        data = load(file)
    return data

def save_to_json_file(my_obj, filename):
    """Saves data to a JSON file."""
    with open(filename, 'w') as file:
        dump(my_obj, file)

def main():
    """Main function."""
    filename = 'add_item.json'
    args = sys.argv[1:]

    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    main()

