#!/usr/bin/python3
"""
    This module defines a "Rectangle" class.
    The Rectangle class contains the methods
    for instantiating a rectangle object of a
    certain size.
"""


class Rectangle:
    """
        This is the definition of a class "Rectangle".
        It contains the definition of the methods
        for instantiating a rectangle object
    """
    def __init__(self, width=0, height=0):
        """
            This is the init method of this rectangle class

            Args:
                width: The width of the rectangle
                height: The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
            This is the area method
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            This is the perimeter method
        """
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)


    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
    
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
