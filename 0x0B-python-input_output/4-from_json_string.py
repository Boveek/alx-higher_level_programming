#!/usr/bin/python3
"""Defines a JSON object representation function."""

import json
def from_json_string(my_str):
    """Return the JSON representation of object."""
    return json.loads(my_str)
