
import random


class HashFunction:
    def __init__(self, prime, universeSize, hashTableSize):
        self.a = 1
        self.b = 0
        self.prime = prime
        self.universeSize = universeSize
        self.hashTableSize = hashTableSize

    def apply(self, x):
        return ((self.a * x + self.b) % self.prime) % self.hashTableSize

    def set_random_parameters(self):
        self.a = random.randrange(1, self.prime)  # range 1..p-1
        self.b = random.randrange(self.prime)     # range 0..p-1


def mean_bucket_size(setOfKeys, hashFunction):
    # generate array
    hashTable = []
    for i in range(hashFunction.hashTableSize):
        hashTable.append(None)

    for element in setOfKeys:
        index = hashFunction.apply(element)
        # print("adding element (" + str(element) + ") at " +
        #       str(index))
        if hashTable[index] is None:
            hashTable[index] = list()
        hashTable[index].append(element)

    count = 0
    for element in hashTable:
        # print("bucket [" + str(count) + "] lenght = " +
        #       str(len(element)))
        if element is not None:
            count += 1

    for element in hashTable:
        output = ""
        if element is None:
            output = "None"
        else:
            for listElement in element:
                output += str(listElement) + ","
        # print(output)

    return len(setOfKeys) * 1.0 / count


def estimate_c_for_single_set(setOfKeys, hashFunction):
    best_c_value = None
    for i in range(1000):
        hashFunction.set_random_parameters()
        meanBucketSize = mean_bucket_size(setOfKeys, hashFunction)
        # from E <= 1 + c * |S| / m, with E = meanBucketSize,
        # |S| = len(setOfKeys), m = hashTableSize
        c_value = (meanBucketSize - 1) * hashFunction.hashTableSize /\
            len(setOfKeys)

        # print("c: " + str(c_value) + "; E: " + str(meanBucketSize) +
        #       "; size: " + str(hashFunction.hashTableSize) +
        #       "; len: " + str(len(setOfKeys)))
        # print("a: " + str(hashFunction.a) + "; b: " +
        #       str(hashFunction.b))
        if best_c_value is None or best_c_value > c_value:
            best_c_value = c_value

    return best_c_value


def estimate_c_for_multile_sets(keySetCount, keyCount, hashFunction):
    minC = None
    maxC = None
    meanC = 0

    for i in range(keySetCount):
        keyList = create_random_universe_subset(keyCount,
                                                hashFunction.
                                                universeSize)
        currentC = estimate_c_for_single_set(keyList, hashFunction)
        if minC is None or minC > currentC:
            minC = currentC
        if maxC is None or maxC < currentC:
            maxC = currentC
        meanC += currentC

    meanC = meanC / keySetCount
    return [minC, maxC, meanC]


def create_random_universe_subset(keyCount, universeSize):
    keyList = list()
    for i in range(keyCount):
        keyList.append(random.randrange(universeSize))
    return keyList


def exercise_1():
    # universe: 0...100000
    universeSize = 100000
    prime = 100003
    countOfKeys = 4000
    keyList = list()
    hashTableSize = 500

    # generate random list of keys
    for i in range(countOfKeys):
        keyList.append(i)  # random.randrange(universeSize))

    hashFunc = HashFunction(prime, universeSize, hashTableSize)
    hashFunc.set_random_parameters()

    meanBucketSize = mean_bucket_size(keyList, hashFunc)

    print("exercise 1:")
    print("universe: 0.." + str(universeSize - 1))
    print("prime: " + str(prime))
    print("hashTableSize: " + str(hashTableSize))
    print("HashFunction: ((" + str(hashFunc.a) + " * x + " +
          str(hashFunc.b) + ") mod " + str(prime) + ") mod " +
          str(hashTableSize))
    print("mean bucket size is " + str(meanBucketSize) + "\r\n")


def exercise_2():
    universeSize = 95
    prime = 97
    countOfKeys = 95
    keyList = list()
    hashTableSize = 60

    # generate random list of keys
    for i in range(countOfKeys):
        keyList.append(i)  # random.randrange(universeSize))

    hashFunc = HashFunction(prime, universeSize, hashTableSize)

    best_c_value = estimate_c_for_single_set(keyList, hashFunc)

    print("exercise 2:")
    print("universe: 0.." + str(universeSize - 1))
    print("prime: " + str(prime))
    print("hashTableSize: " + str(hashTableSize))
    print("best c value is " + str(best_c_value) + "\r\n")


def exercise_3():
    universeSize = 95
    prime = 97
    countOfKeys = 75
    hashTableSize = 60
    keySetCount = 10

    hashFunc = HashFunction(prime, universeSize, hashTableSize)

    result = estimate_c_for_multile_sets(keySetCount, countOfKeys,
                                         hashFunc)

    print("exercise 3:")
    print("universe: 0.." + str(universeSize - 1))
    print("prime: " + str(prime))
    print("count of keys: " + str(countOfKeys))
    print("count of key sets: " + str(keySetCount))
    print("hashTableSize: " + str(hashTableSize))
    print("min c: " + str(result[0]))
    print("mean c: " + str(result[2]))
    print("max c: " + str(result[1]))


def exercise_4():
    universeSize = 100
    prime = 101
    countOfKeys = 20
    hashTableSize = 100
    keySetCount = 1000

    hashFunc = HashFunction(prime, universeSize, hashTableSize)

    result = estimate_c_for_multile_sets(keySetCount, countOfKeys,
                                         hashFunc)

    print("exercise 4 (universal):")
    print("universe: 0.." + str(universeSize - 1))
    print("prime: " + str(prime))
    print("count of keys: " + str(countOfKeys))
    print("count of key sets: " + str(keySetCount))
    print("hashTableSize: " + str(hashTableSize))
    print("min c: " + str(result[0]))
    print("mean c: " + str(result[2]))
    print("max c: " + str(result[1]) + "\r\n")

    universeSize = 100
    prime = 10
    countOfKeys = 20
    hashTableSize = 100
    keySetCount = 1000

    hashFunc = HashFunction(prime, universeSize, hashTableSize)

    result = estimate_c_for_multile_sets(keySetCount, countOfKeys,
                                         hashFunc)

    print("exercise 4 (not universal):")
    print("universe: 0.." + str(universeSize - 1))
    print("prime: " + str(prime))
    print("count of keys: " + str(countOfKeys))
    print("count of key sets: " + str(keySetCount))
    print("hashTableSize: " + str(hashTableSize))
    print("min c: " + str(result[0]))
    print("mean c: " + str(result[2]))
    print("max c: " + str(result[1]))


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
