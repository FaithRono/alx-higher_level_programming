#!/usr/bin/python3
"""
Module - 11-student
Contains a class Student with public attributes and methods.
"""


class Student:
    """Defines a student by first_name, last_name, and age attributes."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with a first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of strings containing attribute name
                If provided, only the listed attributes will be retrieved.
                Defaults to None, in which case all attributes are retrieved.

        Returns:
            dict: A dictionary representation of the Student instance.
                Contains the requested attributes based on the 'attrs' argument
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) /
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): A dictionary representing the attributes
                The dictionary key represents the public attribute name,
                and the dictionary value represents the attribute's value.
        """
        for key, value in json.items():
            setattr(self, key, value)
