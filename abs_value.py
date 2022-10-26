def calculations(number):
    value=abs(number)
    return value,number
def main():
    number=int(input("What is your number>>"))
    value=abs(number)
    calculations(number)
    print("The absolute va lue is",value)
main()