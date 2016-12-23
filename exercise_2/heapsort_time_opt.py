#!/usr/bin/python3

import random
import time
import matplotlib.pyplot as plt


def printHeap(heap):
    output = "["
    for i in range(0, len(heap) - 1, 1):
        output += str(heap[i]) + ", "
    output += (str(heap[len(heap) - 1]) + "]")
    print(output)


def generateList(length):
    randList = list()
    for i in range(length):
        randList.append(random.randrange(length))
    return randList


def repairHeap(heap, index):
    if index < len(heap):
        min = heap[index]
        minIndex = index
        if right(heap, index) is not None and right(heap, index)['value'] < min:
            min = right(heap, index)['value']
            minIndex = right(heap, index)['index']
        if left(heap, index) is not None and left(heap, index)['value'] < min:
            min = left(heap, index)['value']
            minIndex = left(heap, index)['index']
        if index != minIndex:
            heap[index], heap[minIndex] = heap[minIndex], heap[index]  # swap the elements
            repairHeap(heap, minIndex)  # sink element if necessary


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
    heapify(heap)
    
    result = list()
    for i in range(len(heap)):
        result.append(heap[0])
        heap[0] = heap[len(heap) - 1]
        heap.pop(len(heap) - 1)
        repairHeap(heap, 0)  # repair heap beginning at top of heap to sink down new element
    return result


def plotList(timeTable):
    plt.plot(timeTable.keys(), timeTable.values(), 'ro')
    # plt.yscale('log')
    plt.xscale('log')
    plt.show()

if __name__ == "__main__":
    timeTable = {}

    for j in range(5):  # terate through decades
        dec = pow(10, j)
        for i in range(3):  # iterate the steps 1, 2 and 5
            value = (i * i + 1) * dec
            numbers = generateList(value)
            timestamp = time.time()
            result = heapSort(numbers)
            timediff = time.time() - timestamp
            timeTable[value] = int(timediff * 1000)  # ms

            print("sorted " + str(value) + " elements")

    plotList(timeTable)
