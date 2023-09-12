#!/usr/bin/python3
""" A class declaration """


class MyList(list):
    """ A subclass that inherits from parent class list """

    def print_sorted(self):
        """ Function that sorts a list of integer in ascending order """
        print(sorted(self))
