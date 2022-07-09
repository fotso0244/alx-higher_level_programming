#!/usr/bin/python3
def check_item(my_list, item):
    if len(my_list) != 0:
        for i in my_list:
            if i == item:
                return 1
    return 0


def complex_delete(a_dictionary, value):
    if len(a_dictionary) != 0:
        i = 0
        list_tup = a_dictionary.items()
        for k, v in list(list_tup):
            if v == value:
                del a_dictionary[k]
    return a_dictionary
