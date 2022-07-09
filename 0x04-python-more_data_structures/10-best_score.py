#!/usr/bin/python3
def best_score(a_dictionary):
    i = 0
    key = None
    if a_dictionary is not None:
        item = a_dictionary.items()
        for x in item:
            if x[1] > i:
                i = x[1]
                key = x[0]
    return key
