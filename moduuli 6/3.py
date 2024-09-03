#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def gallons(litras):
    gallonit = litras * 3.785
    return gallonit

inputti = 3

while inputti >= 0:

    inputti = int(input("litrat kiitos "))
    if inputti <= 0:
        break
    gallonit = gallons(inputti)
    print (gallonit)