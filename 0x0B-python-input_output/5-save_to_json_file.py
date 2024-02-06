#!/usr/bin/python3
"""This module contains a function that writes an Object to a text file, using
   a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename=""):
    """This is a function that writes an Object to a text file, using a JSON
       representation:
    """
    text = json.dump(my_obj, ensure_ascii=False)
    with open(filename, mode="w") as myFile:
        if (text):
            myFile.write(text)
        else:
            myFile.write("")
