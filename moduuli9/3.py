class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus_rn= 0, kuljettu_km=2000):
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

    def kulje(self, aika):
        self.kuljettu_km = aika * self.nopeus_rn + self.kuljettu_km



Autofr = Auto("ABC-123", 142)
Autofr.kiihdytä(60)
Autofr.kulje(1.5)
Autofr.print()