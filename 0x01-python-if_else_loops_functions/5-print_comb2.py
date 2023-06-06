#!/usr/bin/python3
for number in range(0, 100):
    if number != 100:
        print("{:02}{}".format(number, ", " if number != 99 else ""), end="")
