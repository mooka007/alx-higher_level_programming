#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
output = abs(number) % 10
if number < 0:
    output = -output
    print(f"Last Digit of {number:d} is {output:d} and is ", end="")
if output > 5:
    print("greater than 5")
elif output == 0:
    print("0")
else:
    print("less than 6 and not 0")
