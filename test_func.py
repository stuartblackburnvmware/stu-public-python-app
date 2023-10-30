# test_func.py

import unittest
from func import app  # Import the Flask app

class TestFunc(unittest.TestCase):
    def test_main_returns_expected_output(self):
        # Test the main function
        with app.test_client() as client:
            response = client.get('/')
            data = response.data.decode('utf-8')
            expected_output = "This is the greatest PUBLIC Python app ever written. Trust me."
            self.assertEqual(data, expected_output)

if __name__ == '__main__':
    unittest.main()

