#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tuple_str = len(sentence), None
        return tuple_str
    tuple_str = len(sentence), sentence[0]
    return tuple_str
