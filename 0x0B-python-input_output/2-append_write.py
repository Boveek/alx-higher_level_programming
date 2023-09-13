#!/usr/bin/python3
""" Define a function that appends a string """


def append_write(filename="", text=""):
    """
    Args:
        filename (str): The name of the file to write.
        text (str): The text to append to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as filee:
        return filee.write(text)
    filee.closed
