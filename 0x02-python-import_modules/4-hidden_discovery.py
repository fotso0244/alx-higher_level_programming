#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list_names = dir(hidden_4)
    for x in list_names:
        if x[0:2] != "__":
            print(x)
