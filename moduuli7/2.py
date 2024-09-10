#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
#Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
#Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.
from operator import truediv

nimet = set()

while True:
    inputti = input("Enter a word: ")

    if inputti == '':
        break
    if inputti in nimet:
        print("That word is already taken.")
    else:
        print("That word is new")
        nimet.add(inputti)

for i in nimet:
    print(i)


