#!/bin/python3

# https://www.geeksforgeeks.org/remove-duplicates-from-a-string-in-o1-extra-space

import doctest


def remove_duplicates(string):
    """
    >>> remove_duplicates('abcdabdcda')
    'abcd'
    >>> remove_duplicates('abcdefgabcdefghij')
    'abcdefghij'
    >>> remove_duplicates('abcdefklmgabcdefghij')
    'abcdefklmghij'
    """
    counter = 0
    old_len, new_len = len(string), 0

    for s in string:
        index = ord(s) - 97
        # If char is not present in counter it means it is coming first time
        # Add the char into a string and increase len and mark the counter bit
        if counter & (1 << index) == 0:
            counter = counter | (1 << index)
            string = string[0:new_len] + s + string[new_len + 1:old_len]
            new_len += 1

    return string[0:new_len]


if __name__ == '__main__':
    doctest.testmod()

    s = str(input())

    res = remove_duplicates(s)

    print(res)
