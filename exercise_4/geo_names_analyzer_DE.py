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


def compute_most_frequent_city_names_by_sorting_DE():
    """ get most frequnet city name by sorting
    """

    nameList = []
    count = 0
    for element in read_info_from_file():
        # if count > 50000:
        #     break
        count += 1
        elementFound = False
        code = element[1]
        if count % 1000 == 0:
            # printing length of names in list and total count
            # of localities parsed
            print(str(len(nameList)) + ", " + str(count))
        for existingElement in nameList:
            if existingElement[0] == element[0]:
                if code == 'DE':
                    existingElement[2] = True
                existingElement[1] += 1
                # index of element found, increase occurrence
                # and break loop
                elementFound = True
                break
        if not elementFound:
            if code == 'DE':
                # element not yet in list and belongs to DE
                # -> append element with occurrence = 1
                nameList.append([element[0], 1, True])
            else:
                # element not yet in list but does not belong to DE
                # -> append element with occurrence = 1
                nameList.append([element[0], 1, False])

    nameList = [element for element in nameList if element[2] == True]
    nameList.sort(key=lambda x: x[1])
    nameList.reverse()

    return nameList



if __name__ == "__main__":
    #fileName = "../AT.txt"
    fileName = "../allCountries.txt"

    result = compute_most_frequent_city_names_by_sorting_DE()
    if len(result) > 0:
        print(result[0][0] + "  " +
            str(result[0][1]))
    if len(result) > 1:
        print(result[1][0] + "  " +
            str(result[1][1]))
    if len(result) > 2:
        print(result[2][0] + "  " +
            str(result[1][1]))

