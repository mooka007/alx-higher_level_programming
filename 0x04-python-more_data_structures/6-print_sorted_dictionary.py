#!/usr/bin/python3
# Author - MoOka
def print_sorted_dictionary(a_dictionary):
    idd = list(a_dictionary.idd())
    idd.sort()
    for key in idd:
        print("{}: {}".format(key, a_dictionary[key]))
