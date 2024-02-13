#!/usr/bin/python3
"""This is the module that contains the 'Square' class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the 'Square' class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """This is the str magic method for 'print' statements to work with"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """This method updates the instance attributes of a square object"""
        attr_list = ["id", "size", "x", "y"]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for i, arg in enumerate(args):
                setattr(self, str(attr_list[i]), arg)

    def to_dictionary(self):
        """This method generates a dict based on the attribute-values of a
           rectangle instance
        """
        sqr_dict = dict(id=self.id, x=self.x, size=self.size, y=self.y)
        return sqr_dict

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is int:
            self.__width = width
        else:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is int:
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is int:
            self.width = size
            self.height = size
            self.__size = size
        else:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
