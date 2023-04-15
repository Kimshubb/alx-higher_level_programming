#!/usr/bin/python3
# import functions  does some maths and prints the result
if __name__ == "__main__":
    import calculater_1.py
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} ={}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print(f"{} / {} = {}".format(a, b div(a, b)))
