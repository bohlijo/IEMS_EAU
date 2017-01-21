import random
import time

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild

    def setRightChild(self, rightChild):
        self.rightChild = rightChild

    def setValue(self, value):
        self.value = value

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def toString(self):
        stringRight = "None"
        stringLeft = "None"
        if self.getRightChild() is not None:
            stringRight = self.getRightChild().toString()
        if self.getLeftChild() is not None:
            stringLeft = self.getLeftChild().toString()

        stringResult = "[(" + str(self.key) + ", \"" + str(self.value) \
                       + "\"), left: " + stringLeft \
                       + ", right: " + stringRight + "]"
        return str(stringResult)


class BinarySearchTree():
    def __init__(self):
        self.firstNode = None

    def insert(self, key, value):
        """ function to insert node
        >>> searchTree = BinarySearchTree()
        >>> searchTree.insert(12, "test")
        >>> searchTree.toString()
        [(12, "test"), left: None, right: None]

        >>> searchTree = BinarySearchTree()
        >>> searchTree.insert(1, "test1")
        >>> searchTree.insert(5, "test5")
        >>> searchTree.toString()
        [(1, "test1"), left: None, right: [(5, "test5"), left: None, right: None]]
        """
        if self.firstNode is None:
            self.firstNode = TreeNode(key, value)
        else:
            parentForInsertion = self.findInsertionNode(key)
            if parentForInsertion is None:
                print("error")
            else:
                if key > parentForInsertion.getKey():
                    parentForInsertion.setRightChild(TreeNode(key, value))
                    # print("right " + str(parentForInsertion.getKey()) + " " + str(key) + " " + str(value))
                elif key < parentForInsertion.getKey():
                    parentForInsertion.setLeftChild(TreeNode(key, value))
                    # print("left " + str(parentForInsertion.getKey()) + " " + str(key) + " " + str(value))
                else:
                    parentForInsertion.setValue(value)
                    # print("change " + str(parentForInsertion.getKey()) + " " + str(key) + " " + str(value))

    def findInsertionNode(self, key):
        parentNode = None
        currentNode = self.firstNode
        # if firstNode is None while loop is never run, None is returned
        while currentNode is not None:
            parentNode = currentNode
            if key > currentNode.getKey():
                currentNode = currentNode.getRightChild()
            elif key < currentNode.getKey():
                currentNode = currentNode.getLeftChild()
            else:
                # currentNode has searched key, stop passing down tree
                break
        return parentNode

    def lookup(self, key):
        currentNode = self.firstNode
        # if firstNode is None while loop is never run, None is returned
        while currentNode is not None:
            if key > currentNode.getKey():
                currentNode = currentNode.getRightChild()
            elif key < currentNode.getKey():
                currentNode = currentNode.getLeftChild()
            else:
                # currentNode has searched key, stop passing down tree
                break
        return currentNode

    def toString(self):
        if self.firstNode is None:
            print("empty")
        else:
            print(str(self.firstNode.toString()))


def Insert_n_random_elements(n):
    searchTree = BinarySearchTree()
    for i in range(n):
        randomValue = random.randrange(n)
        searchTree.insert(randomValue, str(randomValue))


def Insert_n_elements(n):
    searchTree = BinarySearchTree()
    for i in range(n):
        searchTree.insert(i, str(i))

if __name__ == "__main__":
    for i in range(10, 15, 1):
        n_value = 2 ** i
    
        timestamp = time.time()
        Insert_n_random_elements(n_value)
        timediff = time.time() - timestamp
        print("Insert_n_random_elements(" + str(n_value) + "): " + str(timediff))

        timestamp = time.time()
        Insert_n_elements(n_value)
        timediff = time.time() - timestamp
        print("Insert_n_elements(" + str(n_value) + "): " + str(timediff))
