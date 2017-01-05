#!/usr/bin/python3

import random
import time
import matplotlib.pyplot as plt


def printHeap(heap):
    """ function print the given heap to the command line

    >>> printHeap([24, 6, 12, 32, 18])
    [24, 6, 12, 32, 18]

    >>> printHeap("hello")
    Traceback (most recent call last):
        ...
    TypeError: input is not a list

    >>> printHeap([])
    empty list
    """

    if not type(heap) == list:
        raise TypeError("input is not a list")
    if len(heap) == 0:
        print("empty list")
        return

    output = "["
    for i in range(0, len(heap) - 1, 1):
        output += str(heap[i]) + ", "
    output += (str(heap[len(heap) - 1]) + "]")
    print(output)


def generateRandomList(length):
    randList = list()
    for i in range(length):
        randList.append(random.randrange(length))
    return randList


def repairHeap(heap, index):
    if index < len(heap):
        min = heap[index]
        minIndex = index
        if right(heap, index) is not None and \
                right(heap, index)['value'] < min:
            min = right(heap, index)['value']
            minIndex = right(heap, index)['index']
        if left(heap, index) is not None and \
                left(heap, index)['value'] < min:
            min = left(heap, index)['value']
            minIndex = left(heap, index)['index']
        if index != minIndex:
            # swap the elements
            heap[index], heap[minIndex] = heap[minIndex], heap[index]
            # sift element if necessary
            repairHeap(heap, minIndex)


def heapify(heap):
    lastParent = len(heap) - 1
    for index in range((lastParent - 1)//2, -1, -1):
        repairHeap(heap, index)


def right(heap, index):
    rightIndex = index * 2 + 2
    if rightIndex < len(heap):
        return {'value': heap[rightIndex], 'index': rightIndex}
    else:
        return None


def left(heap, index):
    leftIndex = index * 2 + 1
    if leftIndex < len(heap):
        return {'value': heap[leftIndex], 'index': leftIndex}
    else:
        return None


def heapSort(heap):
    """ function to sort an input list with heapsort algorithm

    >>> heapSort([24, 6, 12, 32, 18])
    [6, 12, 18, 24, 32]

    >>> heapSort([1, 1, 1, 1, 1])
    [1, 1, 1, 1, 1]

    >>> heapSort("hello")
    Traceback (most recent call last):
        ...
    TypeError: input is not a list

    >>> heapSort([])
    empty list
    """

    if not type(heap) == list:
        raise TypeError("input is not a list")
    if len(heap) == 0:
        print("empty list")
        return

    heapify(heap)

    result = list()
    for i in range(len(heap)):
        result.append(heap[0])
        heap[0] = heap[len(heap) - 1]
        heap.pop(len(heap) - 1)
        # repair heap beginning at top of heap to sink down new element
        repairHeap(heap, 0)
    return result


def plotList(timeTable):
    plt.plot(timeTable.keys(), timeTable.values(), 'ro')
    # plt.yscale('log')
    plt.xscale('log')
    plt.show()

if __name__ == "__main__":
    timeTable = {}

    # calculation steps (uncomment the desired value):
    # sortingCount = 2  # 1, 2, 5, 10, 20, 50
    # sortingCount = 3  # 1, 2, 5, 10, ..., 100, 200, 500
    sortingCount = 4  # 1, 2, 5, 10, ..., 1000, 2000, 5000
    # sortingCount = 5  # 1, 2, 5, 10, ..., 10000, 20000, 50000
    # sortingCount = 6  # 1, 2, 5, 10, ..., 100000, 200000, 500000

    for j in range(sortingCount):  # iterate through decades
        dec = pow(10, j)
        for i in range(3):  # iterate the steps 1, 2 and 5
            value = (i * i + 1) * dec
            numbers = generateRandomList(value)
            timestamp = time.time()
            result = heapSort(numbers)
            timediff = time.time() - timestamp
            timeTable[value] = int(timediff * 1000)  # ms

            print("sorted " + str(value) + " elements in "
                  + str(timeTable[value]) + " ms")
            # printHeap(result)

    plotList(timeTable)
