#!/usr/bin/python3
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new_file = "add_item.json"
args = sys.argv[1:]

with open(new_file, mode="r") as myFile:
    if not myFile.read():
        save_to_json_file(new_obj, new_file)
loaded = load_from_json_file(new_file)
new_obj = list(loaded) + args
