import random


def randomyser():
    numero = random.randint(1, 6)
    return numero

numero = 0
while numero != 6:
    numero = randomyser()
    print(numero)