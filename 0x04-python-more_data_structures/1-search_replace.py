#!/usr/bin/python3
def find_indexes(list_ch, item):
    indexes = []
    for idx, value in enumerate(list_ch):
        if value == item:
            indexes.append(idx)
    return indexes


def search_replace(my_list, search, replace):
    index = find_indexes(my_list, search)
    copy_list = list.copy(my_list)
    if len(index) != 0:
        for i in index:
            copy_list[i] = replace
    return copy_list
