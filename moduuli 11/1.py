class Julkaisu:
    def __init__(self,name):
        self.name = name
    def tulosta(self):
        print(f"{self.name}:")

class Kirja(Julkaisu):

    def __init__(self, name, writer, pages):
        super().__init__(name)
        self.writer = writer
        self.pages = pages


    def printdetails(self):
        super().tulosta()
        print(self.writer, self.pages)

class Lehti(Julkaisu):

    def __init__(self,name, publisher):
        self.publisher = publisher
        super().__init__(name)
    def printdetails(self):
        super().tulosta()
        print( self.publisher)

julkaisut = []

julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 100))
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))

for t in julkaisut:
    t.printdetails()