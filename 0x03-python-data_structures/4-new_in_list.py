#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0 or idx > len(my_list) - 1):
        cop_list = list.copy(my_list)
        return cop_list
    else:
        cop_list = list.copy(my_list)
        cop_list[idx] = element
        return cop_list
