#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence != None and len(sentence) != 0):
        length = len(sentence)
        first = sentence[0]
    else:
        length = 0
        first = None
    return length, first
