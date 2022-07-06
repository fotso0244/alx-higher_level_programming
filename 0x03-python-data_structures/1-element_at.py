#!/usr/bin/python3
def element_at(my_list, idx):
    try:
        if (idx < 0 or idx > len(my_list)):
            print("None")
        else:
            return my_list[idx]
    except:
        print("An error occured")
