#!/usr/bin/python3
def check_item(my_list, item):
    if len(my_list) != 0:
        for i in my_list:
            if i == item:
                return 1
    return 0


def simple_delete(a_dictionary, key=""):
    a_list = list(a_dictionary)
    if (len(a_list) != 0 and key != ""):
        if (check_item(a_list, key) == 1):
            del a_dictionary[key]
    return a_dictionary
