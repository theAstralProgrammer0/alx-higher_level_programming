#!/usr/bin/python3
"""This module contains a function that writes an Object to a text file, using
   a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """This is a function  that writes an Object to a text file, using a JSON
       representation:
    """
    text = json.dumps(my_obj, ensure_ascii=False)
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
