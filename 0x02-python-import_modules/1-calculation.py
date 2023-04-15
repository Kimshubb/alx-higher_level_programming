#!/usr/bin/python
# import functions from calculator_1.py does some maths and prints the result
import calculater_1.py
a = 10
b = 5
sum_result = add(a, b)
subtraction_result = subtract(a, b)
multiplication_result = multiply(a, b)
division_result = divide(a, b)
print(f"{a} + {b} is {sum_result}")
print(f"{a} - {b} is {subtraction_result}")
print(f"{a} * {b} is {multiplication_result}")
print(f"{a} / {b} is division_result")
