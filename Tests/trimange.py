import unittest
from triangles import is_triangle

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("These sticks would make a triangle :)",is_triangle(3,3,3))  # add assertion here


if __name__ == '__main__':
    unittest.main()
