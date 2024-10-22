##Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h).Jos nopeuden muutos on
# negatiivinen, auto hidastaa. Metodin on muutettava auto-olion
# nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta
# suuremmaksi eikä alentua nollaa  pienemmäksi. Jatka pääohjelmaa siten,
# että auton nopeutta nostetaan ensin  +30 km/h, sitten +70 km/h ja lopuksi +50
# km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä
# nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei
# tarvitse vielä päivittää

class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus_rn= 0, kuljettu_km=0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus_rn = nopeus_rn
        self.kuljettu_km = kuljettu_km

    def print(self):
        print(self.rekisteri, self.huippunopeus,
              " tämän hetkenen nopeus", self.nopeus_rn,
              " kuljettu matka", self.kuljettu_km )

    def kiihdytä(self, muutos):
        muutos = int(muutos)
        if (self.nopeus_rn + muutos) < 0:
            self.nopeus_rn = 0
        elif (self.nopeus_rn + muutos) < self.huippunopeus:
            self.nopeus_rn = self.nopeus_rn + muutos
        elif(self.nopeus_rn + muutos) > self.huippunopeus:
            self.nopeus_rn = self.huippunopeus






Autofr = Auto("ABC-123", 142)
Autofr.kiihdytä(620)
Autofr.print()