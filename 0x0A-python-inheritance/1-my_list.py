#!/usr/bin/python3
"""Creates my own list.

Illustrates the concept of Inheritance in Python. For
this unit, we'll be creating a subclass MyList from the
superclass list & perform some operations on it.
Awesome :)

"""


class MyList(list):
    """Defines my own list.

    Args:
        list ('obj':'class':'list'): List class

    """

    def print_sorted(self):
        """Return a sorted list.

        We'll make a copy of the list then sort the list copy
        and print the sorted out list.

        Returns:
            sorted_list ('obj':'list':'int'): The sorted list.

        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
