import unittest
from even_odd import even_or_odd


class MyTestCase(unittest.TestCase):
    def test_even_odd(self):
        self.assertEqual("13 is an odd number",even_or_odd(num))


    # In the space below, write a test function for bonus. Make sure to import the appropriate information
    # at the top of this file. Make sure to write three test cases.
    def test_bonus(self):
        # when you are ready to write your tests, go ahead and delete pass
        def even_or_odd(number):

            if number % 2 == 1:
                print(number, "is an odd number")
            if number % 2 == -1:
                print(number, "is an odd number")
            if number % 2 == 0:
                print(number, "is an even number")

        def main():
            number = int(input("What is your number?>>"))
            even_or_odd(number)

        main()




if __name__ == '__main__':
    unittest.main()
