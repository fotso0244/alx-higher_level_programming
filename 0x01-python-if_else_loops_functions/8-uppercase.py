#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        test = (len(str) != 0 and ord(str[i]) <= 122 and ord(str[i]) >= 97)
        print("{}".format(chr(ord(str[i])
                          - 32)) if test else "{}".format(str[i]), end='')
        if (len(str) != 0 and i == len(str) - 1):
            print("", end='\n')
