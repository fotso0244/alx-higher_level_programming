#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if (j != i and (10 * i + j < 10 * j + i)):
            if (i == 8 and j == 9):
                print("{}{}".format(i, j))
            else:
                print("{}{}, ".format(i, j), end='')
