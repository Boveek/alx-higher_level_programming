#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    num = len(my_list)
    if idx >= num:
        return None
    return (my_list[idx])
