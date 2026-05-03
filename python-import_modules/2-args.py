#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg = len(argv) - 1
    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(arg))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
