#!/usr/bin/python3
def uppercase(str):
    upper = ""
    counter = 0
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            x = ord(i)
            x = x - 32
            character = chr(x)
            upper = upper + character
        else:
            upper = upper + str[counter]
        counter = counter + 1
    print("{}".format(upper))
