#!/usr/bin/env python3

import unittest
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient  # Assuming the class is defined in client.py

class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.GithubOrgClient.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that the org method returns the expected result."""

        # Create a mock response object for the get_json method
        mock_response = Mock()
        mock_response.json.return_value = {"login": org_name, "id": 12345}  # Mocked response
        mock_get_json.return_value = mock_response

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org()

        # Assert that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Assert that the returned result matches the mock response
        self.assertEqual(result, mock_response.json.return_value)


if __name__ == "__main__":
    unittest.main()
