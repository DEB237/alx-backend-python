#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient  # Assuming GithubOrgClient is implemented in client.py

class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.GithubOrgClient.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that the org method returns the expected result."""
        
        # Setup mock return value for get_json
        mock_response = Mock()
        mock_response.return_value = {"login": org_name, "id": 12345}  # Example mock response
        mock_get_json.return_value = mock_response
        
        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org()
        
        # Assert that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Assert that the returned result matches the mock response
        self.assertEqual(result, mock_response)

if __name__ == "__main__":
    unittest.main()
