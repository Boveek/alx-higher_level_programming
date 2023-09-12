#!/usr/bin/python3
""" A class declaration """


def lookup(obj):
    """ Available attributes and methods of an object.

    Args:
    obj: The object input to be checked.

    Returns:
    list of available attributes and methods of the object.
    """

    return dir(obj)
