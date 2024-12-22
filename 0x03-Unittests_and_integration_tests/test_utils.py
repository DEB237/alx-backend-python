#!/usr/bin/env python3

import unittest
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the utils.access_nested_map function.
    """

    def test_access_nested_map(self):
        # Test cases for valid paths
        nested_map = {"a": 1}
        path = ("a",)
        self.assertEqual(access_nested_map(nested_map, path), 1)

        nested_map = {"a": {"b": 2}}
        path = ("a",)
        self.assertEqual(access_nested_map(nested_map, path), {"b": 2})

        nested_map = {"a": {"b": 2}}
        path = ("a", "b")
        self.assertEqual(access_nested_map(nested_map, path), 2)

    def test_access_nested_map_exception(self):
        # Test cases for invalid paths
        nested_map = {}
        path = ("a",)
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(path))

        nested_map = {"a": 1}
        path = ("a", "b")
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(path))

if __name__ == "__main__":
    unittest.main()
