import random
class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus_rn= 0, kuljettu_km=0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus_rn = nopeus_rn
        self.kuljettu_km = kuljettu_km

    def printd(self):
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

    def kulje(self, aika):
        self.kuljettu_km = aika * self.nopeus_rn + self.kuljettu_km
lista = []

for i in range(1, 11):
    auto = (Auto("ABC-"+str(i),random.randint(100,200)))
    lista.append(auto)
    auto.printd()

while True:
    for i in lista:
        auto.kiihdytä(random.randint(-15,15))
        auto.kulje(i)