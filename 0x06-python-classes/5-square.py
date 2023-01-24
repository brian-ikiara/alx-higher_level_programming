#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Instantiate the private attribute called size.

        Args:
            size (int): Square size.

        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """Get the square's size.

        Returns:
            Size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size.

        Args:
            value (int): Value to be set.

        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculate the square's area.

        Returns:
            The square's area.

        """
        return self.__size ** 2

    def my_print(self):
        """Print a square based on value of size."""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()
