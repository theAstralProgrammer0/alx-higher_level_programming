#!/usr/bin/python3
"""This module contains the 'Base' class and will be the “base” of all
   other classes in this project. The goal of it is to manage id attribute in
   all your future classes and to avoid duplicating the same code
   (by extension, same bugs)
"""
import json
import csv


class Base:
    """This is the 'Base' class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This method initializes an instance of the 'Base' class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=[]):
        """This is the serialization function"""
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """This is the deserialization function"""
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs=[]):
        """This is the file i/o handling function to save the json string from
           a list of python dictionaries
        """
        new_list_objs = [obj.to_dictionary() for obj in list_objs]
        text = cls.to_json_string(new_list_objs)
        with open("{}.json".format(cls.__name__), "w") as f:
            if list_objs:
                f.write(text)
            else:
                f.write('[]')

    @classmethod
    def create(cls, **dictionary):
        """This is a method that creates a new instance from key word args"""
        dummy = cls(22, 22, 22, 22)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """This is a method that deserializes JSON object to a Python object"""
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                json_string = f.read()
        except Exception:
            return []
        else:
            dict_objs = cls.from_json_string(json_string)
            instance_list = [cls.create(**dic) for dic in dict_objs]
            return instance_list


"""
    @classmethod
    def save_to_file_csv(cls, list_objs):


    @classmethod
    def load_from_file_csv(cls):
"""
