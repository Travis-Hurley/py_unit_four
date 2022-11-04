#Travis Hurley-oct/31-sample problems
import random

def plus(number1,number2):
    '''
    runs the addition equation and prints
    :param number1:
    :param number2:
    '''
    user_responce_plus=input(str(number1)+"+"+str(number2)+"=")
    answer_addition=number1+number2
    if int(user_responce_plus)==int(answer_addition):
        print("Congratulations! That is correct!!")
    else:
        print("Oh no! The answer was "+str(answer_addition)+". That is ok! Try again.")
def sub(number1,number2):
    '''
    runs the subtraction equation
    :param number1:
    :param number2:
    :return:
    '''
    user_responce_sub = input(str(number1) + "-" + str(number2) + "=")
    answer_subtractaction = number1 - number2
    if int(user_responce_sub) == int(answer_subtractaction):
        print("Congratulations! That is correct!!")
    else:
        print("Oh no! The answer was " + str(answer_subtractaction) + ". That is ok! Try again.")
def multi(number1,number2):
    '''
    runs multiplication equation
    :param number1:
    :param number2:
    '''
    user_responce_multi = input(str(number1) + "*" + str(number2) + "=")
    answer_multiplacation = number1 * number2
    if int(user_responce_multi) == int(answer_multiplacation):
        print("Congratulations! That is correct!!")
    else:
        print("Oh no! The answer was " + str(answer_multiplacation) + ". That is ok! Try again.")

def kind(equation,number1,number2):
    '''
    identifies type of equation
    :param equation:
    :param number1:
    :param number2:
    '''
    if equation=="multiplication":
        multi(number1, number2)
    elif equation=="subtraction":
        sub(number1,number2)
    else:
        plus(number1,number2)


def main():
    '''
    defines variables and runs kind
    '''
    equation = (input("Would you prefer addition, subtraction, or multiplication?"))
    large = int(input("What is the maximum number you would like to use?"))
    small = int(input("What is the minimum number you would like to use"))
    number1 = random.randint(small,large)
    number2 = random.randint(small,large)
    kind(equation, number1, number2)
main()
