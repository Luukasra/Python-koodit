import math
vuosi = int(input("Mikä vuosiluku on "))

if vuosi % 100 == 0 and vuosi % 400 != 0:
    print("ei")
elif vuosi % 400 == 0:
    print("on")
elif vuosi % 4 == 0:
    print("on")
else:
    print("ei")
