#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#check whether the number is positive or zero or negative
if number > 0:
	print(number, "is positive")
elif number < 0:
	print(number, "is negative")
else:
	print(number, "is zero")
