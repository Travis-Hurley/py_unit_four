#Travis Hurley-oct/31-sample problems
import random

def plus(number1,number2):
    user_responce_plus=input(str(number1)+"+"+str(number2)+"=")
    answer_addition=number1+number2
    if int(user_responce_plus)==int(answer_addition):
        print("Congradulations! Thats correct!!")
    else:
        print("Oh no! The answer was "+str(answer_addition)+" Thats ok! Try again.")
def sub(number1,number2):
    user_responce_sub = input(str(number1) + "-" + str(number2) + "=")
    answer_subtractaction = number1 - number2
    if int(user_responce_sub) == int(answer_subtractaction):
        print("Congradulations! Thats correct!!")
    else:
        print("Oh no! The answer was " + str(answer_subtractaction) + " Thats ok! Try again.")
def multi(number1,number2):
    user_responce_multi = input(str(number1) + "*" + str(number2) + "=")
    answer_multiplacation = number1 * number2
    if int(user_responce_multi) == int(answer_multiplacation):
        print("Congradulations! Thats correct!!")
    else:
        print("Oh no! The answer was " + str(answer_multiplacation) + " Thats ok! Try again.")

def kind(equation,number1,number2):
    if equation=="multiplacation":
        multi(number1, number2)
    elif equation=="subtraction":
        sub(number1,number2)
    else:
        plus(number1,number2)


def main():
    equation =(input("Would you prefer +, -, or *?"))
    large = int(input("What is the maximum number you would like to use?"))
    small = int(input("What is the minimum number you would like to use"))
    if large>20 and small>5:
        number1=random.randint(small,20)
        number2=random.randint(small,20)
    elif large<20 and small>5:
        number1 = random.randint(small, large)
        number2 = random.randint(small, large)
    elif small<5 and large<20:
        number1 = random.randint(5, large)
        number2=random.randint(5,large)
    kind(equation,number1,number2)
main()

