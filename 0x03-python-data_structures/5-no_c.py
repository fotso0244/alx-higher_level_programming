#!/usr/bin/python3
def no_c(my_string):
    cop_string = my_string
    if (my_string is not None):
        cop_string = cop_string.translate({ord('c'): None})
        cop_string = cop_string.translate({ord('C'): None})
    return cop_string
