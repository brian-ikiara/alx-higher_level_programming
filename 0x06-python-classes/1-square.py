#!/usr/bin/python3
"""Defines a square based on size.

Example:
    >>> Square = __import__('1-square').Square
    >>> my_square = Square(3)
    >>> print(type(my_square))
    <class '1-square.Square'>
    >>> print(my_square.__dict__)
    {'_Square__size': 3}
    >>> try:
    >>> ....print(my_square.size)
    >>> except Exception as e:
    >>> ....print(e)
    'Square' object has no attribute 'size'
    >>> try:
    >>> ....print(my_square.__size)
    >>> except Exception as e:
    >>> ....print(e)
    'Square' object has no attribute '__size'

"""


class Square:
    """Represents a square.

    Attributes:
        none

    """

    def __init__(self, __size):
        """Initialize the size private instance attribute.

        Args:
            size (int): The size of the square

        """
        self.__size = __size
