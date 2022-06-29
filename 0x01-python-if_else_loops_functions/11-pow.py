#!/usr/bin/env python3
def pow(a, b):
    if b == 0:
        return 1
    res = 1
    if b > 0:
        for i in range(1, b + 1):
            res = res * a
    else:
        b = b * -1
        for i in range(1, b + 1):
            res = res * a
        res = 1 / res
    return res
