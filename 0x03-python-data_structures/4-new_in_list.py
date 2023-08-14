#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    num = len(my_list)
    if idx < 0:
        return my_list
    if idx >= num:
        return my_list
    my_list[idx] = element
    return my_list
