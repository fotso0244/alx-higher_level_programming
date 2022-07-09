#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dict = a_dictionary.copy()
    if len(a_dictionary) != 0:
        for k, v in copy_dict.items():
            del copy_dict[k]
            copy_dict[k] = v * 2
    return copy_dict
