#!/usr/bin/python3
'''defines a rectangle class'''


class Rectangle:
    '''represent a rectangle'''

    def __init__(self, width=0, height=0):
        '''initializze the rectangle
        ARGS: height(int)
              width(int)
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''gets the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''validates data'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''encapsulates data'''
        return self.__height

    @height.setter
    def height(self, value):
        '''validates data'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns the area'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''returns the perimeter'''
        return ((self.__width * 2) + (self.__height * 2))
