#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    try:
        if (len(my_list) != 0 and my_list is not None):
            for i in range(len(my_list)):
                print("{:d}".format(my_list[(i + 1) * -1]))
    except:
        print("An error occured")
