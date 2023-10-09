#!/usr/bin/python3
'''Rectangle class that inherits from base'''

from models.base import Base
'''Defines class Rectangle
    private instance height and weight 
'''
class Rectangle(Base):
    def __init__(self, width, height,x=0, y=0, id=None):
        '''Initialize a new Rectangle
        Args: width-
               height-
               x - x coordinates of new rectangle
               y - y coordinates of new rectangle
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''get the width of the Rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the width of new rectangle'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''get the height of new rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height of new rectangle'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        '''sets the x coordinate'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self, y):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.height * self.width
    def display(self):
        '''prints out the rectangle using #'''
        if self.width == 0 or self.height == 0:
            print("")
            return
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
    def __str__(self):
        '''Overide the __str__ method to return a formatted string'''
        return "[Rectangle] (<id>) <x>/<y> - <width>/<height>".format(self.id, self.x, self.y, self.width, self.height)
     def update(self, *args):
	     if args:
		     if len(args) >= 1:
			     self.id = args[0]
		     if len(args) >= 2:
		             self.width = args[1]
	     	     if len(args) >= 3:
		             self.height = args[2]
	             if len(args) >= 4:
		             self.x = args[3]
	     	     if len(args) >= 5:
		             self.y = args[4]
