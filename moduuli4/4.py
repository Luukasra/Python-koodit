import random

luku = int(input("arvaa luku "))

oikealuku = random.randint(1, 10)

while luku != oikealuku:

    if(luku >= oikealuku):
        print("luku on pienempi ")

    elif(luku < oikealuku):
        print("luku on isompi ")

    luku = int(input("arvaa luku "))
print("way to go")