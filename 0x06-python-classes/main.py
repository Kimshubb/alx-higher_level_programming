#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(9)
my_square_1.my_print()
print("______")

my_square_2 = Square()
my_square_2.size = Square(3)
my_square_2.position = (3,2)
my_square_2.my_print()
print("______")

my_square_3 = Square(0)
my_square_3.size = Square(1)
my_square_3.position = (2,4)
my_square.my_print()
print("............")


