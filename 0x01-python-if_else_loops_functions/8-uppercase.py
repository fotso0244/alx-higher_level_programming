#!/usr/bin/python3
def uppercase(str):
    if (len(str)):
        for i in range(0, len(str)):
            test = (ord(str[i]) <= 122 and ord(str[i]) >= 97)
            print("{}".format(chr(ord(str[i])
                              - 32)) if test else "{}".format(str[i]), end='')
            if (len(str) and i == len(str) - 1):
                print("", end='\n')
    else:
        print("", end='')
