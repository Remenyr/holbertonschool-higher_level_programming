#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Tets max_integer in some cases
    """
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 4, 0]), 4)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([-2, -4, -6]), -2)
        self.assertAlmostEqual(max_integer([3, 1, 3]), 3)
        self.assertAlmostEqual(max_integer([100]), 100)
