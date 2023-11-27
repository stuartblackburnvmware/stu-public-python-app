import unittest
from server import app  # Import the Flask app

class TestFunc(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def test_main_returns_expected_output(self):
        # Make a request to the '/' endpoint
        response = self.app.get('/')

        # Check if the response contains the expected string
        expected_output = "This is the greatest PUBLIC python app ever written. Trust me."
        self.assertIn(expected_output, response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
