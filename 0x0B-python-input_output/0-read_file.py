#!/usr/bin/python3

""" Defines the function read"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.

    Note:
        You must use the 'with' statement.
        You don’t need to manage file permission or file doesn'texist exception
        You are not allowed to import any module.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')

# Test the function

if __name__ == "__main__":
    read_file("my_file_0.txt")
