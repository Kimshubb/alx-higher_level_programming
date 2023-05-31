#!/usr/bin/bash
'''Class defination'''
class Square:
    '''Class square attributes'''
    def __init__(self, size=0):
        '''Initialize a square
        Args - size int -size of the square
        '''
        self.size = size

    @property
    def size(self):
        '''get the current size of the square'''
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        ''' Return the current areaof the square'''
        return(self.__size **2)
    def my_print(self):
        '''Print the square with # character'''
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
        

