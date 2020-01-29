#!/bin/python3

import doctest


def sortRadix(arr):
    """
    >>> sortRadix([9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> sortRadix([1, 0, 123, 321, 987, 765, 4321, 6656, 836, 976, 999])
    [0, 1, 123, 321, 765, 836, 976, 987, 999, 4321, 6656]
    >>> sortRadix([0, 222, 999, 875, 98765, 3456, 87654, 887665, 54543])
    [0, 222, 875, 999, 3456, 54543, 87654, 98765, 887665]
    """
    length = len(arr)

    # Get longest len of nums
    digits = 0
    for i in range(length):
        arr[i] = str(arr[i])
        lt = len(arr[i])
        digits = lt if (lt > digits) else digits

    # Add zero's in front of all numbers lesser then digits
    for i in range(length):
        lt = len(arr[i])
        if lt < digits:
            # Get no. of zero's to be added and add them in front
            zeros = digits - lt
            arr[i] = (zeros * '0') + arr[i]

    # Sort numbers using passes and buckets
    for passes in range(digits):
        bucket = {}
        for i in arr:
            key = i[digits - passes - 1]
            if key in bucket:
                bucket[key] += [i]
            else:
                bucket[key] = [i]
        # Add nums back in the array
        arr = []
        for key in range(10):
            arr += bucket[str(key)] if str(key) in bucket else []

    # Remove zero's from front of nums
    arr = [int(i) for i in arr]

    return arr


if __name__ == '__main__':
    doctest.testmod()

    arr = eval(input())

    res = sortRadix(arr)
    print (res)
