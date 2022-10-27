import unittest
from exams import gets_a_zero


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("True",gets_a_zero(100,50))  # add assertion here


if __name__ == '__main__':
    unittest.main()