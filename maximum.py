import random
a=random.randint(1,10)
b=random.randint(1,10)
def max(a,b):
    print("a is",a)
    print("b is",b)
    if a>b:
        print(a)
    if a<b:
        print(b)
    else:
        print("equal")
max(a,b)