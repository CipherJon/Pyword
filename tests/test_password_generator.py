import unittest
import string
from generator.password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password_length(self):
        password = generate_password(10)
        self.assertEqual(len(password), 10)

    def test_generate_password_symbols(self):
        password = generate_password(10, include_symbols=True)
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_generate_password_numbers(self):
        password = generate_password(10, include_numbers=True)
        self.assertTrue(any(char.isdigit() for char in password))

    def test_generate_password_uppercase(self):
        password = generate_password(10, include_uppercase=True)
        self.assertTrue(any(char.isupper() for char in password))

    def test_generate_password_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(0)

if __name__ == "__main__":
    unittest.main()