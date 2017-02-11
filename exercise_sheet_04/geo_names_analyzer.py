#!/usr/bin/python3

import time
import os.path

# global file definition
fileName = ""


def read_info_from_file():
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


def compute_most_frequent_city_names_by_sorting():
    """ get most frequnet city name by sorting
    """

    if type(fileName) != str:
        raise ValueError("global variable 'fileName' ist not of type string")

    if not os.path.exists(fileName):
        raise ValueError("file does not exist")

    nameList = []
    for element in read_info_from_file():
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

    return nameList


def compute_most_frequent_city_names_by_map():
    """ get most frequnet city name by map
    """

    nameList = {}
    for element in read_info_from_file():
        if element[0] in nameList:
            nameList[element[0]] += 1
        else:
            nameList[element[0]] = 1

    nameListUnsorted = []
    for element in nameList:
        nameListUnsorted.append([element, nameList[element]])

    nameListUnsorted.sort(key=lambda x: x[1])
    nameListUnsorted.reverse()

    return nameListUnsorted


def compare_runtimes():
    timestamp = time.time()
    mostFrequentNames_Sorting = \
        compute_most_frequent_city_names_by_sorting()
    timediff = time.time() - timestamp
    if len(mostFrequentNames_Sorting) < 3:
        print("not enough localities found")
    else:
        print(mostFrequentNames_Sorting[0][0] + "  " +
              str(mostFrequentNames_Sorting[0][1]))
        print(mostFrequentNames_Sorting[1][0] + "  " +
              str(mostFrequentNames_Sorting[1][1]))
        print(mostFrequentNames_Sorting[2][0] + "  " +
              str(mostFrequentNames_Sorting[1][1]))
    print("time elapsed (Sort.): " + str(int(timediff * 1000)) + " ms")
    # time diff in ms

    timestamp = time.time()
    mostFrequentNames_Map = \
        compute_most_frequent_city_names_by_map()
    timediff = time.time() - timestamp
    if len(mostFrequentNames_Map) < 3:
        print("not enough localities found")
    else:
        print(mostFrequentNames_Map[0][0] + "  " +
              str(mostFrequentNames_Map[0][1]))
        print(mostFrequentNames_Map[1][0] + "  " +
              str(mostFrequentNames_Map[1][1]))
        print(mostFrequentNames_Map[2][0] + "  " +
              str(mostFrequentNames_Map[1][1]))
    print("time elapsed (Map): " + str(int(timediff * 1000)) + " ms")
    # time diff in ms

if __name__ == "__main__":
    #  fileName = "../AT.txt"
    fileName = "../allCountries.txt"

    compare_runtimes()
