#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s1 = a_dictionary.items()
    sort_s1 = sorted(s1)
    if len(sort_s1) != 0:
        for i in sort_s1:
            print(i[0], i[1], sep=": ")
