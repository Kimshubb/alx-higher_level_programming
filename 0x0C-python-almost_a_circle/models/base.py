#!/usr/bin/python3
'''Defines a base class'''


class Base:
    '''base class for all other classes in this project
        __nb_objects= Number of instantiated bases
    '''
    __nb_objects = 0
    def __init__(self, id=None ):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects+=1
            self.id = Base.__nb_objects
