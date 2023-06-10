#!/usr/bin/python3
# Author - MoOka
def new_in_list(my_list, idx, element):
    toz = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        toz[idx] = element
        return toz
