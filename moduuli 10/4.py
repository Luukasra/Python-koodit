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

class Kilpailu:
    def __init__(self, nimi, pituuskm, autot):
        self.nimi = nimi
        self.pituuskm = pituuskm
        self.autot = autot


    def tunti_kuluu(self):
        for Auto in self.autot:
            nopeusmuutos = random.randint(-10, 15)
            Auto.kiihdytä(nopeusmuutos)
            Auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'rekkari':<10} {'max sped':<10} {'Nopeusrn':<10} {'kilsat':<10}")
        for auto in self.autot:
            print(f"{auto.rekisteri:<10} {auto.huippunopeus:<10} {auto.nopeus_rn:<10} {auto.kuljettu_km:<10f} km")

    def kilpailu_ohi(self):

        for auto in lista:

            if auto.kuljettu_km >= self.pituuskm:
                return True

        return False

lista = []

for i in range(1, 11):
    huippunopeus = random.randint(100, 200)

    lista.append(Auto("ABC-"+str(i),huippunopeus))

tosi = True

kisa = Kilpailu("Suuri romuralli", 8000, lista)

tunnit = 0
while tosi:
    kisa.tunti_kuluu()
    tunnit = tunnit + 1
    if kisa.kilpailu_ohi() == True:
        print("ohikisa yippyy")
        kisa.tulosta_tilanne()

        break
    if tunnit % 10 == 0:
        kisa.tulosta_tilanne()