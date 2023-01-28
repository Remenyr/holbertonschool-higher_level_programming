#!/usr/bin/python3
import sys

sum = 0
if __name__ == '__main__':
    n = len(sys.argv)

for i in range(1, n):
    sum = sum + int(sys.argv[i])
print("{}".format(sum))
