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
        self.width = width
        self.height = height

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate Rectangle's area.

        Returns:
            The rectangle's area.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate Rectangle's perimeter.

        Returns:
            0: If height == 0 || width == 0
            The perimeter of the rectangle.

        """
        if self.__width > 0 and self.__height > 0:
            return 2 * (self.__width + self.__height)
        return 0

    def __str__(self):
        """Print a square of a given dimension.

        Returns:
            An empty string

        """
        if self.__width > 0 and self.__height > 0:
            rect = []
            for i in range(self.__height):
                [rect.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    rect.append("\n")
            return ("".join(rect))
        else:
            return str()
