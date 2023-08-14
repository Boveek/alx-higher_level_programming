#!/usr/bin/python3
def print_list_integer(my_list=[]):
    num = len(my_list)
    for i in range(num):
        print("{:d}".format(my_list[i]))
