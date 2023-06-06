#!/usr/bin/python3
for number in range(0, 100):
    sep = ", " if number != 99 else " "
    print("{:02}{}".format(number, sep), end="")
