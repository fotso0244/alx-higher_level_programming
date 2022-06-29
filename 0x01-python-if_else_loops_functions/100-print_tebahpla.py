#!/usr/bin/python3
for i in reversed(range(97, 123)):
    print("{}".format(chr(i)) if i % 2 == 0 else "{}".format(chr(i - 32)), end='')
