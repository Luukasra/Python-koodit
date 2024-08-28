import random
numerot = []
summa = 0
numero = int(input("Anna heittojen määrä "))
for index in range(numero):
    numerot.append(int(random.randint(1, 6)))
for numba in numerot:

    summa = summa + numba

print( summa)
