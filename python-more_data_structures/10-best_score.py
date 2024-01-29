#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_key = a_dictionary.keys()[0]
    best_score = a_dictionary[best_key]
    for key in a_dictionary.keys()[1:]:
        if a_dictionary[key] > best_score:
            best_key = key
            best_score = a_dictionary[key]
    return best_key
