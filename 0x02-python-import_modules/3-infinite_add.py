#!/usr/bin/python3
import sys
if __name__ == "__main__":
    res = 0
    length = len(sys.argv)
    if length == 1:
        print("0")
    else:
        for i in range(length):
            if i != 0:
                res += int(sys.argv[i])
        print("{}".format(res))
