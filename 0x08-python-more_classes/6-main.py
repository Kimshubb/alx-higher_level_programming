#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

for i in range(0, 10):
    print(Rectangle.number_of_instances)
    m_1 = Rectangle(12, 4)
    print(Rectangle.number_of_instances)
    
print(Rectangle.number_of_instances)
