##Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus
# , huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista
# kaksi ensin mainittua parametreina saatuihin arvoihin.Uuden auton
# nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123,
# huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus_rn="0", kuljettu_km="0"):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus_rn = nopeus_rn
        self.kuljettu_km = kuljettu_km

    def print(self):
        print(self.rekisteri, self.huippunopeus, self.nopeus_rn + " tämän hetkenen nopeus" , self.kuljettu_km + " kuljettu matka")


Autofr = Auto("ABC-123", 142)

Autofr.print()