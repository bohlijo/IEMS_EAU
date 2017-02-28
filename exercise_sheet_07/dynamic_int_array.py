#!/usr/bin/python3

# import argparse
import numpy as np
import argparse
import time

class DynamicIntArray:
    """Dynamic integer array class implemented with fixed-size numpy array."""

    def __init__(self):
        """Create empty array with length 0 and capacity 1."""
        self._n = 0  # Number of elements in array
        self._c = 1  # Capacity
        self._a = self._create_array(self._c)

    def __len__(self):
        """Return number of elements in the array."""
        return self._n

    def __getitem__(self, i):
        """Return element at index i."""
        # Check for index out of bounds error.
        if not 0 <= i < self._n:
            raise IndexError('index out of bounds')
        return self._a[i]

    def append(self, value):
        """Add integer value to end of array."""
        relocationOccurred = False

        # Check if given value is of integer type.
        if not isinstance(value, int):
            raise TypeError('value is not integer')
        if self._n == self._c:  # time to resize
            # print("relApp " + str(self._n) + "/" + str(self._c) + "->" + str(2 * self._n))
            self._resize(2 * self._n)
            relocationOccurred = True
        self._a[self._n] = value
        self._n += 1

        # print("app " + str(self._n))
        return relocationOccurred

    def _resize(self, new_c):
        """Resize array to capacity new_c."""
        b = self._create_array(new_c)
        for i in range(self._n):
            b[i] = self._a[i]
        # Assign old array reference to new array.
        self._a = b
        self._c = new_c

    def _create_array(self, new_c):
        """Return new array with capacity new_c."""
        return np.empty(new_c, dtype=int)  # data type = integer

    def remove(self):
        """Re move last element from list"""
        relocationOccurred = False
        if self._n > 0:
            # decrease number of elements
            self._n = self._n - 1
            # set value of deleted element to 0
            self._a[self._n] = 0
            # check if reallocation necessary
            if self._n < self._c / 3:
                # print("relDel " + str(self._n) + "/" + str(self._c) + "->" + str(self._n * 3 / 2))
                self._resize(self._n * 3 / 2)
                relocationOccurred = True

            # print("del " + str(self._n))
        return relocationOccurred

def test1():
    print("Test 1")
    n_value = 1000000
    dynArray = DynamicIntArray()

    timestamp = time.time()
    for i in range(n_value):
        dynArray.append(i)
    timediff = time.time() - timestamp
    print("Time for (" + str(n_value) + ") append operations: " +
          str(timediff))


def test2():
    print("Test 2")
    n_value = 1000000
    dynArray = DynamicIntArray()

    for i in range(n_value):
        dynArray.append(i)

    timestamp = time.time()
    for i in range(n_value):
        dynArray.remove()
    timediff = time.time() - timestamp
    print("Time for (" + str(n_value) + ") remove operations: " +
          str(timediff))

def test3():
    print("Test 3")
    timediff = performAlternatingAppenRemove(True, 1000000, 10000000)
    # print("Time for (" + str(10000000) + ") alternating append/remove operations: " + str(timediff))
    print("10000000\t" + str(timediff))
    
    test4()

def test4():
    print("Test 4")
    timediff = performAlternatingAppenRemove(False, 1000000, 10000000)
    #print("Time for (" + str(10000000) + ") alternating remove/append operations: " + str(timediff))
    print("10000000\t" + str(timediff))

def performAlternatingAppenRemove(startWithAppend, startSize, iterationCount):
    # generate array with 1 million elements
    n_value = startSize
    dynArray = DynamicIntArray()
    for i in range(n_value):
        dynArray.append(i)

    # perform 10 million operations
    nextOperationIsAppend = False
    timestamp = time.time()
    for i in range(iterationCount):
        if nextOperationIsAppend:
            nextOperationIsAppend = not dynArray.append(0)
        else:
            nextOperationIsAppend = dynArray.remove()
    timediff = time.time() - timestamp
    return timediff

def testRuntime():
    
    for i in range(8):
        dynArray = DynamicIntArray()
        timestamp = time.time()
        for j in range(10 ** i):
            dynArray.append(0)
        timediff = time.time() - timestamp
        print(str(10 ** i) + "\t" + str(timediff))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=
                                     'Process dynamic array tests.')
    parser.add_argument('--test1', dest='action', action='store_const', const=test1)
    parser.add_argument('--test2', dest='action', action='store_const', const=test2)
    parser.add_argument('--test3', dest='action', action='store_const', const=test3)
    parser.add_argument('--test4', dest='action', action='store_const', const=test4)
    parser.add_argument('--testRuntime', dest='action', action='store_const', const=testRuntime)
    args = parser.parse_args()
    if args.action is not None:
        args.action()
    else:
        print("no arguments given")
