#!/usr/bin/env python3

import unittest
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the utils.access_nested_map function.
    """

    def test_access_nested_map_case_1(self):
        """
        Test that access_nested_map returns the expected result for case 1
        """
        nested_map = {"a": 1}
        path = ("a",)
        self.assertEqual(access_nested_map(nested_map, path), 1)

    def test_access_nested_map_case_2(self):
        """
        Test that access_nested_map returns the expected result for case 2
        """
        nested_map = {"a": {"b": 2}}
        path = ("a",)
        self.assertEqual(access_nested_map(nested_map, path), {"b": 2})

    def test_access_nested_map_case_3(self):
        """
        Test that access_nested_map returns the expected result for case 3
        """
        nested_map = {"a": {"b": 2}}
        path = ("a", "b")
        self.assertEqual(access_nested_map(nested_map, path), 2)

    def test_access_nested_map_exception_case_1(self):
        """
        Test that access_nested_map raises a KeyError for invalid path (case 1)
        """
        nested_map = {}
        path = ("a",)
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(path))

    def test_access_nested_map_exception_case_2(self):
        """
        Test that access_nested_map raises a KeyError for invalid path (case 2)
        """
        nested_map = {"a": 1}
        path = ("a", "b")
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(path))


if __name__ == "__main__":
    unittest.main()
