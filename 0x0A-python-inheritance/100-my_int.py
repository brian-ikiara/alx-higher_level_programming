#!/usr/bin/python3
"""MyInt is a very bad boy."""


class MyInt(int):
    """The terrible twos.

    Args:
        int ('obj':'class'): Superclass

    """

    def __init__(self, num):
        """Instantiate MyInt.

        Args:
            num (int): Number

        """
        self.num = num

    def __ne__(self, val):
        """Is not equal.

        Args:
            val ('obj':'any'): Object

        Returns:
            True.

        """
        return self.num == val

    def __eq__(self, val):
        """Is equal.

        Args:
            val (int): Integer

        Returns:
            False.

        """
        return self.num != val

    def __str__(self):
        """Print number."""
        return str(self.num)
