#!/bin/python3
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
from collections import Counter

import doctest


def isValid(s):
    """
    >>> isValid('aabbcd')
    'NO'
    >>> isValid('aabbccddeefghi')
    'NO'
    >>> isValid('abcdefghhgfedecba')
    'YES'
    >>> isValid('abcc')
    'YES'
    """
    count = Counter(s)

    if len(set(count.values())) == 1:
        return 'YES'
    elif len(set(count.values())) > 2:
        return 'NO'
    else:
        val = list(count.values())
        maximum = max(val)
        minimum = min(val)

        if val.count(maximum) == 1 and maximum - minimum == 1:
            return 'YES'
        elif val.count(minimum) == 1 and minimum == 1:
            return 'YES'
        return 'NO'


if __name__ == '__main__':
    # doctest.testmod()

    s = input()
    result = isValid(s)
    print(result)
