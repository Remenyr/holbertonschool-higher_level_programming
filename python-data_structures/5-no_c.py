#!/usr/bin/python3
def no_c(my_string):
    copy = my_string.translate({ord('c'): "", ord('C'): ""})
    return copy
