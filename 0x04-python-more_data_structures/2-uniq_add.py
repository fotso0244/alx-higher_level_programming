#!/usr/bin/python3
def check_item(my_list, item):
    if len(my_list) != 0:
        for i in my_list:
            if i == item:
                return 1
    return 0


def uniq_items(my_list):
    if len(my_list) != 0:
        uniq = []
        for i in my_list:
            idx = my_list.index(i)
            if (check_item(uniq, my_list[idx]) == 0):
                uniq.append(my_list[idx])
    return uniq


def uniq_add(my_list=[]):
    res = 0
    if len(my_list) != 0:
        uniq = uniq_items(my_list)
        for i in uniq:
            res += i
    return res
