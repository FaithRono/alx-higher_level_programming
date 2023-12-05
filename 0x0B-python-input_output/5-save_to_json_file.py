#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file in JSON format.

    Args:
        my_obj: The object to be written to the file.
        filename: The name of the file to write the object to.

    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
