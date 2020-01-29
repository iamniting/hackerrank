#!/bin/python3

# https://www.codechef.com/problems/TRISQ

import doctest


def getSquareCount(base):
    """
    >>> getSquareCount(1)
    0
    >>> getSquareCount(5)
    1
    >>> getSquareCount(8)
    6
    >>> getSquareCount(10)
    10
    """
    blocks = int(base/2) - 1

    # Sum of first n natural numbers
    res = int((blocks * (blocks+1)) / 2)

    return res


if __name__ == '__main__':
    doctest.testmod()

    n = int(input())
    num = []
    for i in range(n):
        num.append(int(input()))

    for i in num:
        result = getSquareCount(i)
        print (result)
