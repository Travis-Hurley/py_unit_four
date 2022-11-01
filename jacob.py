import random
"""
def who_wins(user, computer):
    if (user == 1 and computer == 1) or (user == 2 and computer == 2) or (user == 3 and computer == 3):
        return "It's a draw!"
    elif (user == 2 and computer == 1) or (user == 3 and computer == 2) or (user == 1 and computer == 3):
        return "You Win!"
    elif (user==1 and computer==2) or (user==2 and computer==3) or (user==3 and computer==1):
        return "You lose!"


def main():
    print("Welcome to rock, paper, scissors!")
    print("Choose your weapon! 1 is rock, 2 is paper, 3 is scissors. Remember, no guns allowed!")
    user = int(input(">>"))
    computer = random.randint(1,3)
    print(user)
    print(computer)
    print(who_wins(user, computer))

if __name__ == '__main__':
    main()
"""
def is_triangle(side1, side2, side3):
    if (side1 + side2 < side3) or (side1 + side3 < side2) or (side2 + side3 < side1):
        return "That's not a triangle!"
    else:
        return "Wow, that's totally triangular bro!"

def main():
    side1 = int(input("What is your first side length?"))
    side2 = int(input("What is your second side length?"))
    side3 = int(input("What is your third side length?"))
    print(is_triangle(side1, side2, side3))

if __name__ == '__main__':
    main()