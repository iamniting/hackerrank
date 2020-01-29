#!/bin/python3

# A number staircase s is an integer number, when read from left to right,
# starts with the number 1, which is followed by a 2, which is followed
# by a 3, and so on. This process continues until a maximum number n is
# reached, which may contain more than one digit. From this point, the
# number staircase s will descend starting at n - 1, then n - 2,
# then n - 3, and so on, until it descends back to 1.

import doctest


def isStairCase(s):
    """
    >>> isStairCase('123456789101110987654321')
    True
    >>> isStairCase('12345678910987654321')
    True
    >>> isStairCase('123321')
    False
    >>> isStairCase('11')
    False
    >>> isStairCase('2')
    False
    """
    if s == '1':
        return True

    if len(s) == 1:
        return False

    length = len(s)
    i = 1
    j = length - 2

    old = int(s[0])
    new = int(s[0])

    r_old = int(s[length-1])
    r_new = int(s[length-1])

    digits = 1
    res = False

    while i <= j:
        if new in (9, 99, 999, 9999, 99999):
            digits += 1

        old = new
        new = int(s[i:i + digits])

        r_old = r_new
        r_new = int(s[-(i + digits):-i])

        if new == r_new and new - old == 1 and r_new - r_old == 1:
            res = True
        else:
            return False

        i = i + digits
        j = j - digits

    if new == int(s[i:i+digits]):
        return False

    return res


if __name__ == '__main__':
    doctest.testmod()

    s = str(input())

    res = isStairCase(s)
    print (res)
