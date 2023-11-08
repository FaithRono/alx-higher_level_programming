#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create an empty dictionary to store the new key-value pairs
    new_dict = {}

    # Iterate through the original dictionary
    for key, value in a_dictionary.items():
        # Create a new key-value pair with the same key and a value that is double the original value
        new_dict[key] = value * 2

    # Return the new dictionary
    return new_dict
