#!/usr/bin/env python3
"""UTF-8 validation module"""


def validUTF8(data):
    """ method that determines if a given data set represents a
        valid UTF-8 encoding.
    """
    bytes_left = 0

    for num in data:
        if bytes_left == 0:
            if num >> 7 == 0b0:   # 1-byte character
                bytes_left = 0
            elif num >> 5 == 0b110:  # 2-byte character
                bytes_left = 1
            elif num >> 4 == 0b1110:  # 3-byte character
                bytes_left = 2
            elif num >> 3 == 0b11110:  # 4-byte character
                bytes_left = 3
            else:
                return False
        else:
            if num >> 6 != 0b10:  # Continuation byte
                return False
            bytes_left -= 1

    return bytes_left == 0
