#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
import sys
def check_op(x):
    """My check operator function

    Args:
        x: an operator

    Returns:
        1 if true, otherwise 0
    """
    res = 0
    list_op = ["+", "-", "*", "/"]
    for c in list_op:
        if c == x:
            return 1
    return res
if __name__ == "__main__":
    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        op = sys.argv[2]
    if (check_op(op) == 0):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if op == "+":
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
        if op == "-":
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
        if op == "/":
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
        if op == "*":
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
