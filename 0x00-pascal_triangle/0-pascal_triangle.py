#!/usr/bin/python3
'''A module that defines Pascal's triangle.
'''


def pascal_triangle(n):
    '''a function that returns a list of lists of integers
    representing the Pascal's triangle of n

    Args:
       n(int) - integer

    Returns:
        list -  empty list if n <= 0
    '''
    pasc_triangle = []
    if type(n) is not int or n <= 0:
        return pasc_triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(pasc_triangle[i - 1][j - 1] + pasc_triangle[i - 1][j])
        pasc_triangle.append(line)
    return pasc_triangle
