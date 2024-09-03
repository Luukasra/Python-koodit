import random


def randomyser(numba):
    numero = random.randint(1, numba)
    return numero

numero = 0
luku = int(input("numero kiitos "))
while numero != luku:
    numero = randomyser(luku)
    print(numero)