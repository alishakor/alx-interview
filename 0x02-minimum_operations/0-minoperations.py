#!/usr/bin/python3
"""The minimum operations coding challenge.
"""


def minOperations(n):
    """
    Computes the fewest number of operations needed to result
    in exactly n H characters.
    Args:
        n(int): number of characters
    Returns:
        operations(int): number of operations else 0
    """
    if not isinstance(n, int):
        return 0
    operations = 0
    clipboard = 0
    prev_h = 1
    # print('H', end='')
    while prev_h < n:
        if clipboard == 0:
            # copy all and paste
            clipboard = prev_h
            prev_h += clipboard
            operations += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - prev_h > 0 and (n - prev_h) % prev_h == 0:
            # copy all and paste
            clipboard = prev_h
            prev_h += clipboard
            operations += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            prev_h += clipboard
            operations += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return operations
