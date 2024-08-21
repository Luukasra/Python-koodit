sukupuoli = input("Onko kyseessä Mies vai Nainen ")
arvo = int(input("Mikä on hemoglobiiniarvo "))

if sukupuoli == "Nainen" and 117 <= arvo <= 175:
    print("arvot aokay")
elif sukupuoli == "Nainen" and 117 >= arvo:
    print("arvot alhaset ")
elif sukupuoli == "Nainen" and 175 <= arvo:
    print("arvot korkeet")

if sukupuoli == "Mies" and 134 <= arvo <= 195:
    print("arvot aokay")
elif sukupuoli == "Mies" and 134 >= arvo:
    print("arvot alhaset ")
elif sukupuoli == "Mies" and 194 <= arvo:
    print("arvot korkeet")