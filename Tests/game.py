import unittest
from guess import calculate

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("Oh no! Thats not right. My number was 3 from your guess. My number was 2", calculate(2,5,3))  # add assertion here


if __name__ == '__main__':
    unittest.main()
