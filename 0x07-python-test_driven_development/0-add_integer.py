#!/usr/bin/python3
def add_integer(a, b=98):
    """ Function that adds two integers.
    Args:
        a: integer or float input to divide
        b: integer or float to be divided by
    Returns:
        An Integer
    Raises:
        TypeError if a or b is not an integer
    """
    if ((not isinstance(a, float) and not isinstance(a, int))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, float) and not isinstance(b, int))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
