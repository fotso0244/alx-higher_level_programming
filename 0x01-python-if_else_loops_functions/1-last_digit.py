#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    mod = ((number * -1) % 10) * -1
else:
    mod = number % 10
print("Last digit of", number, "is", end=' ')
if (mod < 6 and mod != 0):
    print(mod, "and is less than 6 and not 0", end='\n')
if mod > 5:
    print(mod, "and is greater than 5", end='\n')
if mod == 0:
    print(mod, "and is 0", end='\n')
