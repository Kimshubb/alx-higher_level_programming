#!/usr/bin/python3
'''Define Class Square'''
class Square:
    '''Define Square attributes'''
    def __init__(self, size=0):
        ''''instanciate instance attributes
        args: size -must be an integer
        '''
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):
        '''return the current area of the square'''
        return(self.__size * self.__size)

