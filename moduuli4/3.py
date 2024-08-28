numerot = []

numero = input("Anna ensimmäinen numero tai lopeta painamalla Enter: ")
while numero != "":
    numerot.append(int(numero))
    numero = input("Anna seuraava numero tai lopeta painamalla Enter: ")


numerot.sort()
eka = numerot[0]
vika = numerot[-1]
print("eka on " + str(eka) + " vika on " + str(vika))