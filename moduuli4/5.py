
oikeakäyttis = str("python")
oikeasalis = str("rules")
m = 6
while m > 0:
    m = m - 1

    käyttäjätunnus = str(input("Anna käyttis "))
    käyttäjäsalis = str(input("Anna salis "))

    if(oikeasalis == käyttäjäsalis and oikeakäyttis == oikeakäyttis):
        print("tervetuloa")
        break
    elif (m==1):
        print("pääsy evätty ")
        break
    else:
        print("kokeile uudellee")
