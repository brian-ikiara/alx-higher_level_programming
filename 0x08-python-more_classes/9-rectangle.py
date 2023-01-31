#!/usr/bin/python3
"""Program that defines a rectangle."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiate our attributes.

        Args:
            width (int): Rectangle's breadth
            height (int): Rectangle's length

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            r = []
            for i in range(self.__height):
                [r.append(str(self.print_symbol)) for j in range(self.__width)]
                if i != self.__height - 1:
                    r.append("\n")
            return ("".join(r))
        else:
            return str()

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Pay last respects to Rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determine the larger rectangle.

        Args:
            rect_1 (:'obj':'tuple':'int':): First rectangle
            rect_2 (:'obj':'tuple':'int':): Second rectangle

        Raises:
            TypeError: !isinstance((rect_1 || rect_2), Rectangle)

        Returns:
            The larger rectangle.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Make it a square.

        Args:
            size (int): Square size

        Returns:
            A perfect Square!

        """
        cls.__height = size
        cls.__width = size
        return Rectangle(cls.__height, cls.__width)
