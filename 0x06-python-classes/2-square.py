#!/usr/bin/python3
'''Define class Square'''
class Square:
    '''Define class attributes'''
    def __init__(self, size=0):
        '''Initialize a new square
        Args:
            size(int)- size of new square
        '''
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
