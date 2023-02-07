#!/usr/bin/python3
"""Experimenting with Geometry."""


class BaseGeometry:
    """Basic Geometry."""

    def area(self):
        """Raise an error due to non-implementation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer.

        Args:
            name (str): Name
            value (int): Value

        Raises:
            TypeError: !isinstance(value, int)
            ValueError: value <= 0

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines a geometrically accurate rectangle."""

    def __init__(self, width, height):
        """Instantiate a rectangle.

        Args:
            width (int): Rectangle's width
            height (int): Rectangle's height

        """
        if self.integer_validator('width', width):
            self.__width = width
        if self.integer_validator('height', height):
            self.__height = height
