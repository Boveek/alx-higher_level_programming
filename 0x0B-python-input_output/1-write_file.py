#!/usr/bin/python3
""" Defines a file writing function """


def write_file(filename="", text=""):
    """Write to a text file to stdout.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as filee:
        return filee.write(text)
    filee.close
