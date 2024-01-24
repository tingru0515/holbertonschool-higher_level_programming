#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_args = len(argv) - 1
    print("{} argument{}{}".format(num_args, 's' if num_args != 1 else '',
                                   '.' if num_args == 0 else ':'))
    for i in range(1, num_args + 1):
        print("{}: {}".format(i, argv[i]))
