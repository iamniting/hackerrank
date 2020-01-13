#!/bin/python3

# Given a string of the form abc{1}p{2}, expand the string. Remove the
# numbers, & repeat the string before the number as many times as the
# number enclosed in {}

# Sample Input/Output
# Input – ab{2}c  Output –  ababc
# Input – xy{2}bd{2} Output – xyxybdxyxybd
# Input – a{3}b{2} Output – aaabaaab

import doctest


def repeatString(s):
    """
    >>> expandString('ab{2}c')
    'ababc'
    >>> expandString('xy{2}bd{2}')
    'xyxybdxyxybd'
    >>> expandString('a{3}b{2}')
    'aaabaaab'
    >>> expandString('abc{0}def{0}')
    ''
    >>> expandString('abc{0}def{2}')
    'defdef'
    >>> expandString('abc{2}def{0}')
    ''

    """
    string = ''
    num = ''
    flag = False

    for c in s:
        if c == '{':
            flag = True
        elif c == '}':
            flag = False
            string = string * int(num)
            num = ''
        elif flag:
            num = num + c
        else:
            string = string + c
    return string


if __name__ == '__main__':
    doctest.testmod()

    s = input()
    print (repeatString(s))
