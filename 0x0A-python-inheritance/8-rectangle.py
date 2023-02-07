#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a geometrically accurate rectangle."""

    def __init__(self, width, height):
        """Instantiate a rectangle.

        Args:
            width (int): Rectangle's width
            height (int): Rectangle's height

        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
