#!/usr/bin/python3
"""Just have some class."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiate the attributes.

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Lexiconally represent Student."""
        return self.__dict__
