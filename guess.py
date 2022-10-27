import random
def calculate(computer,guess,away):
    if guess!=computer:
        away=abs(computer-guess)
        return ("Oh no! Thats not right.My number was"+str(away)+"from your guess. My number was"+str(guess))


#computer=random.randint(1,10)



