#!/usr/bin/python3
def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    new_list = sorted(list_of_integers)
    return (new_list[- 1])
