#!/bin/python3

# https://www.hackerrank.com/challenges/game-with-cells/problem

import doctest


def gameWithCells(n, m):
    """
    >>> gameWithCells(2, 2)
    1
    >>> gameWithCells(4, 4)
    4
    >>> gameWithCells(7, 6)
    12
    """
    cells4 = int(n/2) * int(m/2)
    cells2 = (m*(n % 2) + n*(m % 2)) / 2
    return int(cells4 + cells2)


if __name__ == '__main__':
    doctest.testmod()

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    result = gameWithCells(n, m)
    print (result)
