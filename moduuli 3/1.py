pituus = int(input("Mikä on kalan pituus senttimetreinä " ))
if pituus<37:
    print("Laittapa se takas vetteen, kalan pitäis olla viel " + str(37-pituus) + " pidempi herra hyvä.")
elif pituus>37:
    print("Syö pois se kala")