#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        tuple_length_char = (0, None)
    else:
        tuple_length_char = (len(sentence), sentence[0])
    return tuple_length_char
