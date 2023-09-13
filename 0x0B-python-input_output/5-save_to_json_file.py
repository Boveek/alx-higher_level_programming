#!/usr/bin/python3
"""Defines a JSON-to-object function."""


import json
def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as filee:
        json.dump(my_obj, filee)
    filee.closed
