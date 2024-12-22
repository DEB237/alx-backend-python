import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient  # Assuming GithubOrgClient is defined in client.py


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
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        # Assert that the returned result matches the mock response
        self.assertEqual(result, mock_response.json.return_value)

    @patch("client.GithubOrgClient.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that the public_repos method returns the expected result."""

        # Sample mock data for public repositories
        mock_response = Mock()
        mock_response.json.return_value = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = mock_response

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the public_repos method
        result = client.public_repos()

        # Assert that get_json was called once with the correct URL for public repos
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google/repos"
        )

        # Assert that the result matches the mock response
        self.assertEqual(result, mock_response.json.return_value)

    @patch("client.GithubOrgClient.get_json")
    def test_public_repos_with_license(self, mock_get_json):
        """Test that the public_repos method returns the expected result with a license filter."""

        # Sample mock data for public repositories with different licenses
        mock_response = Mock()
        mock_response.json.return_value = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = mock_response

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the public_repos method with the 'apache-2.0' license filter
        result = client.public_repos(license="apache-2.0")

        # Assert that get_json was called once with the correct URL and license filter
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google/repos?license=apache-2.0"
        )

        # Assert that the result matches the mock response
        self.assertEqual(result, [
            repo for repo in mock_response.json.return_value
            if repo['license']['key'] == "apache-2.0"
        ])


if __name__ == "__main__":
    unittest.main()
