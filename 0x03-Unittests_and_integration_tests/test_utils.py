import unittest
from unittest.mock import patch, Mock
from utils import get_json  # Assuming get_json is implemented in utils.py

class TestGetJson(unittest.TestCase):
    """
    Test case for the utils.get_json function.
    """

    @patch("requests.get")
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that the get_json function returns the expected result and that the requests.get method is called once.
        """
        # Create a mock response object with a json() method that returns the test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Configure the mock to return our mock_response when called
        mock_get.return_value = mock_response

        # Call the get_json function
        result = get_json(test_url)

        # Assert that requests.get was called exactly once with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the result is equal to the test_payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
