#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiate the size and position attributes.

        Args:
            size (int): Square size.
            position (:obj:`tuple` of :obj:`int`): A point within the square.

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the point in the square.

        Returns:
            The position in the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position to a certain value.

        Args:
            value (int): The coordinate to be set.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the square's area.

        Returns:
            The square's area.

        """
        return self.__size ** 2

    def my_print(self):
        """Print a square based on value of size and position."""
        if self.__size > 0:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()
