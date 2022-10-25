def main():
    print("Lets check if your answer is bigger 20 or smaller than 10!")
    x=int(input("What is your number?>>"))
    if x<10:
        print("Smaller")
    if x>20:
        print("Bigger")
    if 20>=x>=10:
        print("Neither")
    print("finish")
main()