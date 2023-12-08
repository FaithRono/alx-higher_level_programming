#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest
import csv
import json

"""
This module defines the Base class.

The Base class is the "base" of all other classes in the project.
It manages the id attribute and provides a common implementation
for generating unique ids like the ones we are given in the 0-main.py file
"""


class Base:
    """
    The Base class represents the base class for all other
    classes in the project.

    Attributes:
        __nb_objects (int): A private class attribute that keeps track of
        the number of objects created. Used for generating unique ids.
        id (int): A public instance attribute that stores the
        unique id of an object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The id value to assign to the object.
            If provided, the id attribute will be set to this value.
            If not provided, a new unique id will be generated based on
            the __nb_objects attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
