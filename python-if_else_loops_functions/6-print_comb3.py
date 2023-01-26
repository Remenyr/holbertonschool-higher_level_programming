#!/usr/bin/python3
x = 0
for i in range(10):
    if i == 8:
        print("{}{}".format(i, j))
        break
    for j in range(10):
        if j > x:
            print("{}{}".format(i, j), end=", ")
    x = x + 1
