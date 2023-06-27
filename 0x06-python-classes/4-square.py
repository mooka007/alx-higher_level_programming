#!/usr/bin/python3
# Author -MoOka
"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.__size = size

    @property
    def size(self):
        """property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set it"""
        if type(vallue) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
