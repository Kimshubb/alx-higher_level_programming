#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    #exclude the first argument which is always the script name
    args = sys.argv[1:]
    total = sum(map(int, args))
    print(total)
