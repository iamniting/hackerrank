#!/bin/python3

# Find duplicate char in string once

import doctest


def find_duplicate(string):
    """
    >>> find_duplicate('defabcdabcd')
    'dabc'
    >>> find_duplicate('abcdabcd')
    'abcd'
    >>> find_duplicate('abcdabcdabcd')
    'abcd'
    """
    counter, took = 0, 0
    old_len, new_len = len(string), 0

    for s in string:
        index = ord(s) - 97
        # If char is present in a counter and not taken it means coming second
        # time so we need to keep this
        if counter & (1 << index) > 0 and took & (1 << index) == 0:
            # Mark the took bit as true for the char so that we will not take
            # it again if it comes for the third time or so on
            took = took | (1 << index)
            string = string[0:new_len] + s + string[new_len + 1:old_len]
            new_len += 1
        # If char not present in counter mark it in counter
        elif (counter & (1 << index)) == 0:
            counter = counter | (1 << index)

    return string[0:new_len]


if __name__ == '__main__':
    doctest.testmod()

    s = str(input())

    res = find_duplicate(s)

    print (res)
