
class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerrosrn = alinkerros

    def kerros_ylös(self):
        if self.kerrosrn < self.ylinkerros:
            self.kerrosrn = self.kerrosrn + 1

    def kerros_alas(self):
        if self.kerrosrn > self.alinkerros:
            self.kerrosrn = self.kerrosrn - 1

    def siirry_kerrokseen(self, kerros):
        indeks = kerros
        while self.kerrosrn != indeks:
            if self.kerrosrn > kerros:
                self.kerros_alas()
            elif self.kerrosrn < kerros:
                self.kerros_ylös()


class Talo:
    def __init__(self, alinkerros, ylinkerros, hissinmr):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissit = []
        hissinmr = hissinmr +1
        for i in range(1, hissinmr):
            self.hissit.append(Hissi(alinkerros, ylinkerros))





    def aja_hissiä(self, hissinumero, kohde):


        self.hissit[hissinumero].siirry_kerrokseen(kohde)

    def palohalytys(self):
        for i in range(len(self.hissit)):
            self.hissit[i].siirry_kerrokseen(self.alinkerros)
            print(self.hissit[i].kerrosrn)



##pääohjelma

house = (Talo(1,9,3))

house.aja_hissiä(2, 5)
house.palohalytys()