#Travis hurley - oct-27-22

def gets_a_zero(total_classes,class_missed):
    if class_missed>=.25*total_classes: #calculates percent
        return ("FAILED")
    else:
        return ("PASSED")
def main():
    total_classes=int(input("How many classes are you taking?>> ")) #recieves input from user
    class_missed=int(input("How many classes have you missed?>> "))
    print(gets_a_zero(total_classes,class_missed))
main()