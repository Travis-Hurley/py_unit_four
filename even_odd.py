"""
def even_or_odd(number):
    """

"""
    if number%2==0:
        print(int(number),"is an even number")
    else:
        print(int(number), "is an odd number")


def main():
    number=int(input("What is your number?>>"))
    even_or_odd(number)
    # First, make sure to delete the word "pass" then get input from the user.
    # They should type in a number, make sure to convert it to an int
    # Next, call the even_or_odd function, and make sure to pass the user's number as a parameter.


if __name__ == '__main__':
    main()
    """
def even_or_odd(number):
    if number % 2 == 0:
        return (str(number)+" is an even number")
    else:
        return (str(number)+' is an odd number')


def main():
    number = int(input("What is your number?>>"))
    print(even_or_odd(number))


main()
