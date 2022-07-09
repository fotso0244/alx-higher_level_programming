#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    res = 0
    div = 0
    for x in my_list:
        res += x[0] * x[1]
    for x in my_list:
        div += x[1]
    return (res / div)
