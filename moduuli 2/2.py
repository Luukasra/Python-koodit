import math

input = input("mikä on ympyrän säde " )

numero = int(input)

circumference = math.pi * numero ** 2
print("ympyrän pinta-ala on " + str(circumference))