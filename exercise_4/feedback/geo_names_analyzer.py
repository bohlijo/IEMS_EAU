from collections import defaultdict
from timeit import timeit
from zipfile import ZipFile


def read_info_from_file(file):
    """Reads the passed file as zip file and reads all contained files
       as country name database
    """
    localities = []

    with ZipFile(file, 'r') as zip:

        # Iterates all files in the zip file
        # (we could use a static file name instead)
        for fileInZip in zip.namelist():

            # Reads all lines from the file in the zip file
            for line in zip.open(fileInZip):
                data = line.decode('UTF-8').split("\t")

                # Check if valid data row
                if (data[6] == "P" and (int(data[14]) > 0)):

                    # Store only name and country
                    # Tuple (name, country)
                    localities.append((data[1], data[8]))

    return localities


def compute_most_frequent_city_by_sorting(localities):
    """Computes the most frequent city names using sorting"""
    # Sort the list of localities by their name (1st item in tuple)
    # This can also be done via itemgetter
    localities.sort(key=lambda item: item[0])

    locality_occurences = []
    count = 1
    for i in range(len(localities) - 1):
        if localities[i][0] == localities[i + 1][0]:
            count = count + 1
        else:
            locality_occurences.append((localities[i][0], count))
            count = 1

    # Add last city if missing and filter by DE if activated
    if locality_occurences[-1][0] != localities[-1][0]:
        locality_occurences.append((localities[-1][0], count))

    # Sort list by the second item in the tuple
    return sorted(locality_occurences, key=lambda item: item[1], reverse=True)


def compute_most_frequent_city_by_map(localities):
    """Computes the most frequent city names using a hash map"""
    # Creates a dictinary which creates a "0"-entry when no value for the
    # given key was found
    loc_map = defaultdict(int)

    for (loc_name, loc_country) in localities:
        loc_map[loc_name] = loc_map[loc_name] + 1

    # Sort list by the second item in the tuple
    return sorted(loc_map.items(), key=lambda item: item[1], reverse=True)


def compute_most_frequent_city_by_sorting_de(localities):
    """Computes the most frequent city names using sorting only including
       names which occur in germany
    """
    if len(localities) < 1:
        return []

    # Sort the list of localities by their name (1st item in tuple)
    # This can also be done via itemgetter
    localities.sort(key=lambda item: item[0])

    locality_occurences = []
    count = 1
    inDE = (localities[0][1] == 'DE')

    for i in range(len(localities) - 1):
        if localities[i][0] == localities[i + 1][0]:
            count = count + 1
        else:
            if inDE:
                locality_occurences.append((localities[i][0], count))
            count = 1
            inDE = False

        if localities[i + 1][1] == 'DE':
            inDE = True

    # Add last city if missing and filter by DE if activated
    if locality_occurences[-1][0] != localities[-1][0] \
            and (localities[-1][1] == 'DE'):
        locality_occurences.append((localities[-1][0], count))

    # Sort list by the second item in the tuple
    return sorted(locality_occurences, key=lambda item: item[1], reverse=True)


def compute_most_frequent_city_by_map_de(localities):
    """Computes the most frequent city names using a hash map only including
       names which occur in germany
    """
    # Creates a dictinary which creates a "0"-entry when no value for the
    # given key was found
    loc_map = defaultdict(lambda: (0, False))

    for (loc_name, loc_country) in localities:
        tup = loc_map[loc_name]
        loc_map[loc_name] = (tup[0] + 1, tup[1] | (loc_country == 'DE'))

    # Remove the 'DE'-indicator via map
    filtered = map(lambda item: (item[0], item[1][0]),
                   # Filter by 'DE'-indicator (Filter out entries not in DE)
                   filter(lambda item: item[1][1], loc_map.items()))

    # Sort list by the second item in the tuple
    return sorted(filtered, key=lambda item: item[1], reverse=True)


def compare_runtime_setup():
    return read_info_from_file('allCountries.zip')


def compare_runtime():
    # \n is the newline character
    print('Time of sorting:')
    print(timeit(stmt='compute_most_frequent_city_by_sorting(lst)',
           setup='from __main__ import compare_runtime_setup,'
                 + 'compute_most_frequent_city_by_sorting\n'
                 + 'lst = compare_runtime_setup()',
           number=2))

    print('Time of map:')
    print(timeit(stmt='compute_most_frequent_city_by_map(lst)',
           setup='from __main__ import compare_runtime_setup,'
                 + 'compute_most_frequent_city_by_map\n'
                 + 'lst = compare_runtime_setup()',
           number=2))
