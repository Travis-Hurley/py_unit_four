import unittest
from bonus import company_money

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(105.0,company_money(5,100))  # add assertion here


if __name__ == '__main__':
    unittest.main()