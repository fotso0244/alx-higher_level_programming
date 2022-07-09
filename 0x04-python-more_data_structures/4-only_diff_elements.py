#!/usr/bin/python3
def check_item(my_list, item):
    if len(my_list) != 0:
        for i in my_list:
            if i == item:
                return 1
    return 0


def only_diff_elements(set_1, set_2):
    s1 = list(set_1)
    s2 = list(set_2)
    all_uniq = []
    if (len(s1) != 0 or len(s2) != 0):
        for i in s1:
            if (check_item(s2, i) == 0 and check_item(all_uniq, i) == 0):
                all_uniq.append(i)
        for j in s2:
            if (check_item(all_uniq, j) == 0 and check_item(s1, j) == 0):
                all_uniq.append(j)
    return all_uniq
