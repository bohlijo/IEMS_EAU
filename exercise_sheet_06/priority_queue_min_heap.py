#!/usr/bin/python3


class PriorityQueueItem:
    """ Provides a handle for a queue item.
    A simple class implementing a key-value pair,
    where the key is an integer, and the value can
    be an arbitrary object. Index is the heap array
    index of the item.
    """
    def __init__(self, key, value, index):
        self._key = key
        self._value = value
        self._index = index

    def __lt__(self, other):
        """ Enables us to compare two items with a < b.
        The __lt__ method defines the behavior of the
        < (less than) operator when applied to two
        objects of this class. When using the code a < b,
        a.__lt__(b) gets evaluated.
        There are many other such special methods in Python.
        See "python operator overloading" for more details.
        """
        return self._key < other._key

    def get_heap_index(self):
        """ Return heap index of item."""
        return self._index

    def set_heap_index(self, index):
        """ Update heap index of item."""
        self._index = index


class PriorityQueueMinHeap:
    """Priority queue implemented as min heap."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._list = []

    """
    TO DO:
    Create methods:
    insert(self, key, value) -> return inserted item object
    get_min(self) -> return item._key and item._value
    delete_min(self) -> return item._key an item._value
    change_key(item, new_key), no return value
    size() -> return current heap size

    Plus your choice of additional helper (private) methods
    Helpful would be e.g.
    _repair_heap_up(), _repair_heap_down(), _swap_items() ...

    Use private methods (_method_name) if they only get accessed
    within the class.
    Private methods have a leading underscore:
    def _swap_items(self, i, j):
        # Swap items with indices i,j (also swap their indices!)
        ...
    """

    def _getParentIndex(self, index):
        """ returns the parent index of a given index
        >>> p1 = PriorityQueueMinHeap()
        >>> p1._getParentIndex(37)
        18
        >>> p1._getParentIndex(38)
        18
        >>> p1._getParentIndex(0)
        -1
        """
        if index <= 0:
            return -1
        else:
            return (index - 1) // 2  # floor division

    def _getRightChildIndex(self, index):
        return index * 2 + 2

    def _getLeftChildIndex(self, index):
        return index * 2 + 1

    def _getSmallestKeyIndex(self, item):
        parentIndex = item.get_heap_index()
        leftChildIndex = self._getLeftChildIndex(parentIndex)
        rightChildIndex = self._getRightChildIndex(parentIndex)

        smallest = parentIndex

        if leftChildIndex < self.size():
            # at least left child existant
            if self._list[parentIndex]._key >\
               self._list[leftChildIndex]._key:
                smallest = leftChildIndex
            if rightChildIndex < self.size():
                # right child existant
                if self._list[smallest]._key >\
                   self._list[rightChildIndex]._key:
                    smallest = rightChildIndex
        return smallest

    def _getParentItem(self, startItem):
        if startItem.get_heap_index() == 0:
            # no parent present
            return None
        else:
            return self._list[self._getParentIndex(startItem.
                                                   get_heap_index())]

    def _repair_heap_up(self, startItem):
        resultItem = startItem
        parentItem = self._getParentItem(startItem)
        if parentItem is not None:
            if parentItem._key > startItem._key:
                self._swap_items(startItem.get_heap_index(),
                                 parentItem.get_heap_index())
                resultItem = self._repair_heap_up(startItem)
        return resultItem

    def _repair_heap_down(self, startItem):
        resultItem = startItem
        swapIndex = self._getSmallestKeyIndex(startItem)
        if swapIndex != startItem.get_heap_index():
            self._swap_items(swapIndex, startItem.get_heap_index())
            resultItem = self._repair_heap_down(self._list[swapIndex])
        return resultItem

    def _swap_items(self, index_1, index_2):
        """
        >>> pq1 = PriorityQueueMinHeap()
        >>> pq1.insert(1, "first element")._key
        1
        >>> pq1.insert(10, "second element")._key
        10
        >>> unused = pq1.insert(12, "third element")
        >>> unused = pq1.insert(15, "fourth element")
        >>> pq1._list[0]._value
        'first element'
        >>> pq1._swap_items(0, 1)
        >>> pq1._list[0]._value
        'second element'
        """
        temp = self._list[index_1]
        self._list[index_1] = self._list[index_2]
        self._list[index_1].set_heap_index(index_1)
        self._list[index_2] = temp
        self._list[index_2].set_heap_index(index_2)

    def insert(self, key, value):
        # define index of new element (last position of _list)
        index = self.size()
        # create item
        item = PriorityQueueItem(key, value, index)
        # add item to _list
        self._list.append(item)
        # repair heap up from last element
        return self._repair_heap_up(item)

    def get_min(self):
        if len(self._list) > 0:
            return self._list[0]
        else:
            return None

    def delete_min(self):
        """
        >>> pq1 = PriorityQueueMinHeap()
        >>> unused = pq1.insert(1, "first element")
        >>> unused = pq1.insert(10, "second element")
        >>> pq1.size()
        2
        >>> pq1.delete_min()
        >>> pq1.size()
        1
        >>> pq1.delete_min()
        >>> pq1.size()
        0
        >>> pq1.delete_min()
        >>> pq1.size()
        0
        """
        if len(self._list) > 0:
            # move last element to first position
            self._list[0] = self._list[-1]
            self._list[0].set_heap_index(0)
            # pop last element
            self._list.pop()
            # repair heap down from first element (index 0)
            # but only if elements left in list
            if self.size() > 0:
                self._repair_heap_down(self._list[0])

    def change_key(self, item, key):
        """
        >>> pq1 = PriorityQueueMinHeap()
        >>> unused = pq1.insert(1, "first element")
        >>> unused = pq1.insert(10, "second element")
        >>> item3 = pq1.insert(12, "third element")
        >>> unused = pq1.insert(15, "fourth element")
        >>> newItem3 = pq1.change_key(item3, 100)
        >>> newItem3._key
        100
        """
        newKeyIsSmaller = key < item._key
        item._key = key
        if newKeyIsSmaller and item.get_heap_index() != 0:
            # new key is smaller and parent exists: repair up
            return self._repair_heap_up(item)
        else:
            # new key is smaller/equal: repair down
            return self._repair_heap_down(item)

    def size(self):
        return len(self._list)

    def printPriorityHeap(self):
        print("heap size: " + str(self.size()))
        for item in self._list:
            print(str(item._key) + ", " + str(item._value) + " [" +
                  str(item.get_heap_index()) + "]")

if __name__ == "__main__":
    # Create priority queue object.
    pq1 = PriorityQueueMinHeap()
    # Insert some flights into queue.
    pq1_item1 = pq1.insert(1, "Airforce One")
    pq1_item2 = pq1.insert(45, "Bermuda Triangle Blues (Flight 45)")
    pq1_item3 = pq1.insert(666, "Flight 666")
    pq1_item4 = pq1.insert(2, "test")
    pq1.printPriorityHeap()

    unused = pq1.insert(5, "test")
    unused = pq1.insert(12, "test")
    unused = pq1.insert(16, "test")
    unused = pq1.insert(6, "test")
    unused = pq1.insert(100, "test")
    pq1.printPriorityHeap()

    pq1_item4_new = pq1.change_key(pq1_item4, 333)
    pq1.printPriorityHeap()

    print("min value: " + str(pq1.get_min()._value))
    pq1_item1_new = pq1.change_key(pq1_item1, 1000)
    print("min value: " + str(pq1.get_min()._value))
