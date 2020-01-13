#!/bin/python3
# https://www.hackerearth.com/pt-br/problem/algorithm/print-all-substrings/

import doctest


def printSubStringEfficient(string):
    """
    >>> printSubString('abcd')
    a
    b
    c
    d
    ab
    bc
    cd
    abc
    bcd
    abcd
    >>> printSubString('abcde')
    a
    b
    c
    d
    e
    ab
    bc
    cd
    de
    abc
    bcd
    cde
    abcd
    bcde
    abcde
    """
    for i in range(1, len(string) + 1):
        for j in range(0, len(string) + 1 - i):
            print (string[slice(j, j+i)])


def printSubString(string):
    """
    >>> printSubString('abcd')
    a
    b
    c
    d
    ab
    bc
    cd
    abc
    bcd
    abcd
    >>> printSubString('abcde')
    a
    b
    c
    d
    e
    ab
    bc
    cd
    de
    abc
    bcd
    cde
    abcd
    bcde
    abcde
    """
    for i in range(1, len(string)+1):
        for j in range(0, len(string)):
            if j+i < len(string)+1:
                print("".join(string[j:j+i]))


if __name__ == '__main__':
    # doctest.testmod()

    s = input()
    printSubStringEfficient(s)
