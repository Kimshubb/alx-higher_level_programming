#!/usr/bin/python3

def magic_calculation(a, b, c):
    if b < a:
        return(c)
    else:
        if c > b:
            return(a + b)
    else:
        return(a * b - c)
