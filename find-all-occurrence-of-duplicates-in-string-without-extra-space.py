#!/bin/python3

# Find all occurances of duplicate char in string

import doctest


def find_all_occurrence_of_duplicate(string):
    """
    >>> find_all_occurrence_of_duplicate('defabcdabcd')
    'dabcd'
    >>> find_all_occurrence_of_duplicate('abcdabcd')
    'abcd'
    >>> find_all_occurrence_of_duplicate('abcdabcdabcd')
    'abcdabcd'
    """
    counter = 0
    old_len, new_len = len(string), 0

    for s in string:
        index = ord(s) - 97
        # If char already present in counter it means duplicate
        if (counter & (1 << index)) > 0:
            # Add a duplicate in string and increase the len
            string = string[0:new_len] + s + string[new_len + 1:old_len]
            new_len += 1
        # If char not present in counter mark it in counter
        elif (counter & (1 << index)) == 0:
            counter = counter | (1 << index)

    return string[0:new_len]


if __name__ == '__main__':
    doctest.testmod()

    s = str(input())

    res = find_all_occurrence_of_duplicate(s)

    print (res)
