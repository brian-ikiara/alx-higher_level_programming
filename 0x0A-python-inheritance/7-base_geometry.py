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
