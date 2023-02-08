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

    def to_json(self, attrs=None):
        """Lexiconally represent Student.

        Args:
            attrs ('obj':'any'): Student's instance attribute

        Returns:
            Dictionary representation of Student.

        """
        dictStudent = {}
        if attrs is not None:
            for k, v in self.__dict__.items():
                if k in attrs:
                    dictStudent[k] = v
            return dictStudent
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes with JSON.

        Args:
            json ('obj':'JSON'): JSON object

        """
        for k, v in json.items():
            self.__setattr__(k, v)
