#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = list(str)
    for i in range(0, len(str)):
        if i == n:
            cpy[i] = ''
    return "".join(cpy)
