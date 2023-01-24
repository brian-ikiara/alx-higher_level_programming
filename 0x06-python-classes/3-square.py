#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square.

    Demonstrates the various operations that can be performed on
    a square such as Area.

    Attributes:
        size: Square's size.

    """

    def __init__(self, size=0):
        """Instantiate private attribute size.
        
        Args:
            size (int): The size of the square.

        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")


    def area(self):
        """Calculate the square's area.

        Returns:
            The square's area.

        """
        return self.__size ** 2
