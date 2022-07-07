#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv)
    print("{:d} argument{:s}".format(l - 1, "." if l == 1 else "s:"))
    if (l != 1):
        for i in range(l):
            if i != 0:
                print("{:d}: {}".format(i, sys.argv[i]))
