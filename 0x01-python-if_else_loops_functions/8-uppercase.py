#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if (i != len(str) - 1):
            if (ord(str[i]) <= 122 and ord(str[i]) >= 97):
                print(chr(ord(str[i]) - 32), end='')
            else:
                print(str[i], end='')
        if (i == len(str) - 1 and ord(str[i]) <= 122 and ord(str[i]) >= 97):
                print(chr(ord(str[i]) - 32))
        elif i == len(str) - 1:
            print(i)
