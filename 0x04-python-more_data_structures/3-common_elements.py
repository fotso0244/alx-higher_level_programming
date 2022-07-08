#!/usr/bin/python3
def common_elements(set_1, set_2):
    s1 = list(set_1)
    s2 = list(set_2)
    common = []
    if (len(s1) != 0 and len(s2) != 0):
        for i in s1:
            for j in s2:
                if i == j:
                    common.append(i)
    return common
