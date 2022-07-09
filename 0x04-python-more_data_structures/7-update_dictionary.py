#!/usr/bin/python3
def check_item(my_list, item):
    if len(my_list) != 0:
        for i in my_list:
            if i == item:
                return 1
    return 0


def update_dictionary(a_dictionary, key, value):
    a_list = list(a_dictionary)
    if (check_item(a_list, key) == 0):
        a_dictionary[key] = value
    else:
        del a_dictionary[key]
        a_dictionary[key] = value
    return a_dictionary
