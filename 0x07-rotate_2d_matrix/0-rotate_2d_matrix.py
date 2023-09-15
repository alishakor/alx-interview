#!/usr/bin/python3

"""Contains a function that rotates a matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2d matrix
    Args:
        matrix
    Returns:
        Rotated matrix
    """

    duplicated_matrix = [row[:] for row in matrix]
    matrix_size = len(matrix)
    y = -1
    # iterate through each row in the duplicated matrix
    for row in duplicated_matrix:
        # Iterate through each column in the original matrix
        for x in range(matrix_size):
            # update the values of the original matrix with the values
            # from the copied matrix
            matrix[x][y] = row[x]
        # Move to the previous column for the next iteration
        y -= 1
