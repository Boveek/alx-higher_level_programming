#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""
def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    if not list_of_integers:
        return None
    new_list = sorted(list_of_integers)
    return (new_list[- 1])
