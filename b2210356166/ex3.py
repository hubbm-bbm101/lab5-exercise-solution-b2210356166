import random
n=random.randint(1,50)

i=0

while i!=n:
    i=int(input("guess the number"))
    if i>n:
        print("too big, try again")
    elif i<n:
        print("too small, try again")

print("bingo, number is", n)
