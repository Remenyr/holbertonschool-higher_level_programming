#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuplesum = ()
    sum_a = tuple_a + (0, 0)
    sum_b = tuple_b + (0, 0)
    tuplesum = sum_a[0] + sum_b[0], sum_a[1] + sum_b[1]
    return tuplesum
