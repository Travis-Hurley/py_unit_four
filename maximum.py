import random
def max(a,b):
    if a>b:
        return (str(a)+" is larger than "+str(b))
    if a<b:
        return (str(a)+" is smaller than "+str(b))
    else:
        return (str(a)+" is equal to" +str(b))

def main():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    print(max(a,b))
main()
