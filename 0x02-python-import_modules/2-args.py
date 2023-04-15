#!/usr/bin/python3
# program prints the number of as well as list of arguments
if __name__ == "__main__":

    import sys
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 0:
        print("Number of arguments: 0")
    else:
        print("Number of argument(s): {}".format(num_args))
    if num_args == 1:
        print("Argument:")
        print("1: {}".format(args[0]))
    else:
        print("Arguments:")
        for i, arg in enumerate(args):
            print("{}: {}".format(i + 1, arg))
    
