import unittest
from generator.utils import shuffle_string

class TestUtils(unittest.TestCase):
    def test_shuffle_string(self):
        s = "password"
        shuffled = shuffle_string(s)
        self.assertEqual(sorted(s), sorted(shuffled))
        self.assertNotEqual(s, shuffled)

if __name__ == "__main__":
    unittest.main()