#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ A function that divides all elements of a matrix
    Args:
        matrix: The matrix with the element to be divided
        div: The integer to divide the matrix with
    Raises:
        TypeError if matrix is not a matrix (list of lists) of integers/floats
        TypeError if each row of the matrix does not have the same size
        TypeError if div is not a number
        ZeroDivisionError if division by zero
    Returns:
        A new matrix
    """

    if not isinstance(matrix, list):
        raise:
            TypeError(matrix must be a matrix (list of lists) of integers/floats)
    if not isinstance(
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
