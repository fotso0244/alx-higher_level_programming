#!/usr/bin/python3
def no_c(my_string):
    cop_string = my_string
    if (my_string is not None):
        cop_string = my_string.replace("c","")
        cop_string = cop_string.replace("C","")
    return cop_string
