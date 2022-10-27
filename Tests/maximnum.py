import unittest
from maximum import max

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("10 is larger than 9",max(10,9))  # add assertion here


if __name__ == '__main__':
    unittest.main()
