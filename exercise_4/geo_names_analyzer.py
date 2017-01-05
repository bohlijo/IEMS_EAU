#!/usr/bin/python3

import time
import os.path


def read_info_from_file(fileName):
    fobj = open(fileName, "r")

    for line in fobj:
        if line[0] == '#':
            continue
        fields = line.split("\t")
        locality = fields[6]
        inhabitants = fields[14]
        if locality == "P" and inhabitants is not "0":
            name = fields[1]
            code = fields[8]
            yield (name, code)
    fobj.close()


def compute_most_frequent_city_names_by_sorting(fileName):
    """ get most frequnet city name by sorting

    >>> compute_most_frequent_city_names_by_sorting("../AT.txt" + str(123))
    Traceback (most recent call last):
    ...
    ValueError: file does not exist

    >>> compute_most_frequent_city_names_by_sorting(123)
    Traceback (most recent call last):
    ...
    ValueError: parameter 'fileName' ist not of type string

    """

    if type(fileName) != str:
        raise ValueError("parameter 'fileName' ist not of type string")

    if not os.path.exists(fileName):
        raise ValueError("file does not exist")

    nameList = []
    for element in read_info_from_file(fileName):
        elementFound = False
        for existingElement in nameList:
            if existingElement[0] == element[0]:
                existingElement[1] += 1
                # index of element found, increase occurrence
                # and break loop 
                elementFound = True
                break
        if not elementFound:
            # element not yet in list
            # -> append element with occurrence = 1
            nameList.append([element[0], 1])

    nameList.sort(key=lambda x: x[1])
    nameList.reverse()

    print(nameList[0][0] + "  " + str(nameList[0][1]))
    print(nameList[1][0] + "  " + str(nameList[1][1]))

def compute_most_frequent_city_names_by_map(fileName):
    """ get most frequnet city name by map

    >>> compute_most_frequent_city_names_by_map("../AT.txt" + str(123))
    Traceback (most recent call last):
    ...
    ValueError: file does not exist

    >>> compute_most_frequent_city_names_by_map(123)
    Traceback (most recent call last):
    ...
    ValueError: parameter 'fileName' ist not of type string

    """

    if type(fileName) != str:
        raise ValueError("parameter 'fileName' ist not of type string")

    if not os.path.exists(fileName):
        raise ValueError("file does not exist")

    nameList = {}
    for element in read_info_from_file(fileName):
        if element[0] in nameList:
            nameList[element[0]] += 1
        else:
            nameList[element[0]] = 1

    nameListUnsorted = []
    for element in nameList:
        nameListUnsorted.append([element, nameList[element]])
    
    nameListUnsorted.sort(key=lambda x: x[1])
    nameListUnsorted.reverse()
    
    print(nameListUnsorted[0][0] + "  " + str(nameListUnsorted[0][1]))
    print(nameListUnsorted[1][0] + "  " + str(nameListUnsorted[1][1]))


if __name__ == "__main__":
    fileName = "../AT.txt"
    # fileName = "../allCountries.txt"

    timestamp = time.time()
    compute_most_frequent_city_names_by_sorting(fileName)
    timediff = time.time() - timestamp
    print("time elapsed (Sort.): " + str(int(timediff * 1000)) + " ms")
    # time diff in ms

    timestamp = time.time()
    compute_most_frequent_city_names_by_map(fileName)
    timediff = time.time() - timestamp
    print("time elapsed (Map): " + str(int(timediff * 1000)) + " ms")
    # time diff in ms
