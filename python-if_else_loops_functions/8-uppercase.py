#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            result += "{}".format(chr(ord(char) - 32))
        else:
            result += "{}".format(char)
    print(result)
