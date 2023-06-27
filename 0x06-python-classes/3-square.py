#!/usr/bin/python3
# Author - MoOka

class Square:
    """class Square that defines a square"""
    __size = None

    def __init__(self, size=0):
        """Instation with optional size"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("Size must Be >= 0")
        else:
            raise TypeError("size must be an integer")

        def area(self):
            """Public instance method area"""
            return self.__size * self.__size
