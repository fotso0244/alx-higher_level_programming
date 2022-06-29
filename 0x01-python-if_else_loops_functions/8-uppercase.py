#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        test = (ord(str[i]) <= 122 and ord(str[i]) >= 97)
        print(chr(ord(str[i]) - 32) if test else str[i], end='')
        if i == len(str) - 1:
            print("",end='\n')
