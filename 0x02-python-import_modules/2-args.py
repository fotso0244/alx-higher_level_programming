#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    if length == 1:
        print("{:d} argument{:s}".format(length - 1, "s."))
    if length != 1:
        print("{:d} argument{:s}".format(length - 1,
                                         ":" if length == 2 else "s:"))
        for i in range(length):
            if i != 0:
                print("{:d}: {}".format(i, sys.argv[i]))
