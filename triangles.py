def is_triangle(side1, side2, side3):
    if side1+side2<side3 or side2+side3<side1 or side3+side1<side2:
        return ("These sticks would not make a triangle :(")
    else:
        return("These sticks would make a triangle :)")
    return side1,side2,side3
def main():
    side1=int(input("What is the first stick length? >> "))
    side2=int(input("What is the second stick length? >> "))
    side3=int(input("What is the third stick length? >> "))
    print(is_triangle(side1,side2,side3))
if __name__ == '__main__':
    main()