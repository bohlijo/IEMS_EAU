#!/usr/bin/python3

import random


def generateList(length):
    if length > 10000:
        length = 10000

    randList = list()
    for i in range(length):
        randList.append(random.randrange(length))
    return randList


def testIncreasing(lst):
    """ function to test increasing values in lst
    >>> testIncreasing([24, 6, 12, 32, 18])
    'false'

    >>> testIncreasing([])
    'false'

    >>> testIncreasing("Hallo")
    'false'

    >>> testIncreasing([0, 6, 12, 32, 32, 32, 32, 118])
    'true'
    """
    if not type(lst) == list:
        return "false"
    if len(lst) == 0:
        return "false"
    for i in range(1, len(lst), 1):
        if(lst[i] < lst[i - 1]):
            return "false"
    return "true"


def insertionSort(lst):
    """ Sort list using the MinSort algorithm.

    >>> insertionSort([24, 6, 12, 32, 18])
    [6, 12, 18, 24, 32]

    >>> testIncreasing(insertionSort([24, 6, 12, 32, 18]))
    'true'

    >>> insertionSort([])
    []

    >>> insertionSort("hallo")
    Traceback (most recent call last):
        ...
    TypeError: lst must be a list

    """
    # Check given parameter data type.
    if not type(lst) == list:
        raise TypeError('lst must be a list')
    n = len(lst)
    if not n > 0:
        return lst

    sortedList = list()
    sortedList.append(lst[0])

    for i in range(1, n):
        # Find position where to insert value
        for j in range(len(sortedList) + 1):
            if j == len(sortedList):
                # end of sorted list reached, append value to list
                sortedList.append(lst[i])
                break  # break not ecessary here as this is the last iteration
            elif sortedList[j] > lst[i]:
                sortedList.insert(j, lst[i])
                break
    return sortedList


if __name__ == "__main__":
    # Create an unsorted list of integers.
    numbers = generateList(100)
    print(numbers)
    # Sort the list.
    print(insertionSort(numbers))
