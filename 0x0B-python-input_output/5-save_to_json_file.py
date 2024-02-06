#!/usr/bin/python3
"""This module contains a function that writes an Object to a text file, using
   a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """This is a function that writes an Object to a text file, using a JSON
       representation:
    """
    with open(filename, mode="a+") as myFile:
        json.dump(my_obj, myFile)
