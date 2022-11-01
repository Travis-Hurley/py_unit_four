import random
def who_wins(user, computer):
    # 1 is rock, 2 is paper, 3 is scissors
    if (user ==1 and computer==1)or(user==2 and computer==2)or(user==3 and computer==3):
        return "Draw! Try again?"
    elif  (user==1 and computer==3) or (user==2 and computer==1) or (user==3 and computer==2):
        return "You Win! Nice Job!"
    else:
        return "You lose! Nice try..."
def comp(computer):
    if computer==1:
        return("Computer: Rock!")
    elif computer==2:
        return("Computer: Paper!")
    else:
        return("Computer: Scissors!")
def u(user):
    if user==1:
        return("You: Rock!")
    elif user==2:
        return("You: Paper!")
    elif user==3:
        return("You: Scissors!")

def main():
    user=int(input("Rock(1),Paper(2),or Scissors(3)? >> "))
    computer=random.randint(1,3)
    print(u(user))
    print(comp(computer))
    print(who_wins(user,computer))

if __name__ == '__main__':
    main()