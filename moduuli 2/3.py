import math

kanta = int (input("anna kanta " ))
korkeus = int (input("anna korkeus "))

pinta = ((kanta * korkeus)/2)


piiri = (math.sqrt(kanta ** 2 + korkeus ** 2)+ kanta + korkeus)


print( "pinta-ala on " + str(pinta) + " ja piiri on " + str(piiri) + ".")