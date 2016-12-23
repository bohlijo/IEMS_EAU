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


def reapairHeap(heap, index):
    min = heap[index]
    minIndex = index
    if right(heap, index) is not None and right(heap, index)['value'] < min:
        min = right(heap, index)['value']
        minIndex = right(heap, index)['index']
    if left(heap, index) is not None and left(heap, index)['value'] < min:
        min = left(heap, index)['value']
        minIndex = left(heap, index)['index']
    if index != minIndex:
        heap[index], heap[minIndex] = heap[minIndex], heap[index]
        return True
    else:
        return False


def heapify(heap):
    while True:
        changes = False
        for index in range(len(heap)//2 - 1, -1, -1):
            if reapairHeap(heap, index):
                changes = True
        if not changes:
            break


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
    result = list()
    for i in range(len(numbers)):
        result.append(numbers[0])
        numbers[0] = numbers[len(numbers) - 1]
        numbers.pop(len(numbers) - 1)
        heapify(numbers)
    return result


def plotList(timeTable):
    plt.plot(timeTable.keys(), timeTable.values(), 'ro')
    # plt.yscale('log')
    plt.xscale('log')
    plt.show()

if __name__ == "__main__":
    timeTable = {}

    for j in range(3):  # terate through decades
        dec = pow(10, j)
        for i in range(3):  # iterate the steps 1, 2 and 5
            value = (i * i + 1) * dec
            numbers = generateList(value)
            timestamp = time.time()
            heapify(numbers)
            result = heapSort(numbers)
            timediff = time.time() - timestamp
            timeTable[value] = int(timediff * 1000)  # ms

            print("sorted " + str(value) + " elements")

    plotList(timeTable)
