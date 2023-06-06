#!/usr/bin/python3
# Owned By MoOka
for i in range(ord('z'), ord('a') - 1, -1):
        print("{0}".format(chr(i) if i % 2 == 0 else chr(i - 32)), end='')
