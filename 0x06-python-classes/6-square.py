#!/usr/bin/python3

class Square:
    """
    Square class represents a square.

    Attributes:
        __size (int): Size of a side of the square.
        __position (tuple): Position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square.

        Args:
            size (int): Size of a side of the square. Default is 0.
            position (tuple): Position of the square. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or position contains values less than 0.

        Returns:
            None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): Size of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Returns:
            None
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
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): Position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains values less than 0.

        Returns:
            None
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#'.

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
