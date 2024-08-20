import math

input = input("kuinka monta senttimetriä on säde " )

numero = int(input)

circumference = math.pi * numero ** 2
print("ympyrän pinta-ala on " + str(circumference) + "cm")