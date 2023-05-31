#!/usr/bin/python3
'''Define new class Square'''
class Square:
    
    '''Represent Square attributes'''
    def __init__(self, size):
        '''
    Args:
        size - int - size of the new square
        '''
        self.size = size

    @property
    def size(self):
        '''Get the current size of the square'''
        return(self.__size)
    @size.setter
    def size(self, value):
        ''' '''
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >=0")
        self.__size = value

    def area(self):
        '''return the current area of the square'''
        return(self.__size ** 2)


