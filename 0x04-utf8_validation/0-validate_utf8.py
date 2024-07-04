#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    bytes_number = 0

    bitsmask1 = 1 << 7
    bitsmask2 = 1 << 6

    for i in data:

        bitsmask_byte = 1 << 7

        if bytes_number == 0:

            while bitsmask_byte & i:
                bytes_number += 1
                bitsmask_byte = bitsmask_byte >> 1

            if bytes_number == 0:
                continue

            if bytes_number == 1 or bytes_number > 4:
                return False

        else:
            if not (i & bitsmask1 and not (i & bitsmask2)):
                    return False

        bytes_number -= 1

    if bytes_number == 0:
        return True

    return False
