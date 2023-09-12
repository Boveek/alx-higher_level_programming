#!/usr/bin/python3
""" A class declaration """

class MyList(list):
    """ A subclass that inherits from parent class list """

    def print_sorted(self):
        """
        Function that sorts a list of integer in ascending order.

        Returns:
            A sorted list
        """
        sortedd = sorted(self)
        print(sortedd)
