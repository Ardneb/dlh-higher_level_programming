#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) > 0:
        a_dictionary = {key: value for key, value in sorted(a_dictionary.items(), key=lambda item: item[1])}
        return list(a_dictionary.keys())[-1]
    else:
        None
