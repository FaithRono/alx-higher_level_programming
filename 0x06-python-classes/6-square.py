#!/usr/bin/pythoni3
"""Defines a class Square"""


class Square:
    """
    Square class defines a square by size and position.

    Attributes:
        size (int): size of the square.
        position (tuple): position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object.

        Args:
            size (int): size of the square (default is 0).
            position (tuple): position of the square (default is (0, 0)).

        Raises:
            TypeError: if size is not an integer or if position is not a tuple of 2 positive integers.
            ValueError: if size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): size to set.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): position to set.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#' in stdout.

        If the size is equal to 0, it prints an empty line.
        Uses position to adjust the square's position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

