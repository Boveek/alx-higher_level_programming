#!/usr/bin/python3
""" A class representation """


def is_kind_of_class(obj, a_class):
    """ Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object instance to compare.
        a_class: The class to be compared with.

    Returns:
        True if the object is exactly an instance of the specified class 
        and False if otherwise.
    """

    return isinstance(obj, a_class)
