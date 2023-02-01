#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev = my_list
    rev.reverse()
        
    for i in rev:
        print("{}".format(i))