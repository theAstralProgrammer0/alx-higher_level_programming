
#!/usr/bin/python3
"""
    This module defines a "Square" class.
    The Square class contains the methods
    for instantiating a square object of a
    certain size.
    The Square raises exceptions when bad
    values are entered.
    The Square has an area property implementation
"""


class Square:
    """
        Square class contains the __init__
        method that instantiates a square object
        If a bad value is passed, it raises an
        appropriate exception.
        Square class also contains the area method
        that returns the area of the square
    """
    def __init__(self, size=0):
        """
            This is the initializing method for the
            Square class
            Args:
                size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

