#!/usr/bin/python3
"""This is the module that contains the 'Square' class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """This is the 'Square' class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
        
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)
    def update(self, *args, **kwargs):
        attr_list = ["id", "size", "x", "y"]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for i, arg in enumerate(args):
                setattr(self, str(attr_list[i]), arg)

    def to_dictionary(self):
        sqr_dict = dict(id=self.id, x=self.x, size=self.size, y=self.y)
        return sqr_dict

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is int:
            self.height = self.width
            self.__size = size
        else:
            raise TypeError("width must be an integer")
