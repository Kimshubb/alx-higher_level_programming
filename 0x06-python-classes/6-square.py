#!/usr/bin/python3
'''Define a new class Square'''
class Square:
    '''initialize the new square'''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialize the new square
        Args: size - of int type
            raises Typeerror if not integer
            raises Valueerror if less than 0
            '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Gets the size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Sets the size of the square
        Args: valueof int type
        Handle exceptions
        '''
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("size must be greater than 0")
        self.__size = value

    @property
    def position(self):
        '''returns position of the square'''
        return (self.__position)
    @position.setter
    def position(self, value):
        '''
        Sets the position of the square
            Args:
                value tuple-(position to be set)
            raise Type ERROR if value is not a tuple of 2 positive integers

        '''
        if (not isinstance(value, tuple) or len(value) != 2 or not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of two positive integerrs")
        self.__position = value

    def area(self):
        '''calculate the area of a square'''
        return self.__size ** 2

    def my_print(self):
        '''print #  for each value of area'''
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")


    

