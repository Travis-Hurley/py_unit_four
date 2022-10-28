import random
def calculate(computer,guess,away):
    if guess!=computer:
        return str("Oh no! Thats not right. My number was "+str(away)+" from your guess. My number was "+str(computer))
    else:
        return("Yes! That is right. My number was "+str(computer))
    return away
def main():
    guess=int(input("Guess what number I am thinking of >>"))
    str(guess)
    computer=random.randint(1,10)
    away = abs(computer - guess)
    str(away)
    print(str(calculate(computer,guess,away)))
main()



