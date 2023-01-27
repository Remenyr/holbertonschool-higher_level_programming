#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        positive = number * -1
        last = positive % 10
        print("{}".format(last), end="")
        return last
    else:
        last = number % 10
        print("{}".format(last), end="")
        return last
