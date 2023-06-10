#!/usr/bin/pyhton3
# Author - MoOka
def no_c(my_string):
    new_tox = ""
    for char in range(len(my_string)):
        if my_string[char] != 'c' and my_string[char] != 'C':
            new_tox = new_tox + my_string[char]
    return new_tox
