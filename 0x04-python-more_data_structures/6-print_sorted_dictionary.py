#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_d = list(a_dictionary)
    list_d.sort()
    for i in list_d:
        print("{}: {}".format(i, a_dictionary.get(i)))
