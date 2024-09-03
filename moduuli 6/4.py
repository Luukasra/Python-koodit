#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def summalist(lista):
    summa = 0
    for i in lista:
        summa = summa + i


    return summa

lista = []

while True:
    numero = int(input("anna numero tai 0 jos haluut lopettaa: "))
    lista.append(numero)
    if numero == 0:
        break
print(summalist(lista))


