import unittest
from abs_value import calculations

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(4,calculations(4))  # add assertion here


if __name__ == '__main__':
    unittest.main()
