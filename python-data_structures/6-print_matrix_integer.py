#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for number in i:
            print("{:d}".format(number), end=" " if number != i[-1] else "")
        print()
