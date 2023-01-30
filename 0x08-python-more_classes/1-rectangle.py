#!/usr/bin/python3
"""Program that defines a rectangle."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Instantiate our attributes.

        Args:
            width (int): Rectangle's breadth
            height (int): Rectangle's length

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the Rectangle's width.

        Returns:
            The width of the Rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set Rectangle's width to a value.

        Args:
            value (int): New width.

        Raises:
            TypeError: If !int(value)
            ValueError: If value < 0

        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get the Rectangle's height.

        Returns:
            The height of the Rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set Rectangle's height to a value.

        Args:
            value (int): New width.

        Raises:
            TypeError: If !int(value)
            ValueError: If value < 0

        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__height = value
        else:
            raise TypeError("width must be an integer")
