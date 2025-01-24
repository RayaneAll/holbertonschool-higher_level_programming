#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 5, 7, 3]), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -7, -3]), -3)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 3, 7, -5]), 7)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.3, 0.8]), 2.3)

    def test_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable(self):
        with self.assertRaises(TypeError):
            max_integer(42)
