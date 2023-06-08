#!/usr/bin/python3
# Owned By MoOka
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        toto = add(a, b)
        for i in range(4, 6):
            toto = add(toto, i)
        return toto
    else:
        return sub(a, b)
