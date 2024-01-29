#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = list(a_dictionary.keys())[0]
    best_score = a_dictionary[best_key]
    for key in list(a_dictionary.keys())[1:]:
        if a_dictionary[key] > best_score:
            best_key = key
            best_score = a_dictionary[key]
    return best_key
