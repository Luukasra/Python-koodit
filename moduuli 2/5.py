import math

leiviskä = float(input("Anna leiviskät "))
naulat = float(input("Anna naulat "))
luodit = float(input("Anna luodit "))

luodinpaino = 13.3
naulanpaino = 32 * luodinpaino
leiviskänpaino = 20 * naulanpaino

kokopaino = float(luodit * luodinpaino + naulanpaino * naulat + leiviskä * leiviskänpaino)
kilotulos = int(kokopaino / 1000)
grammatulos = int(kokopaino - (kilotulos * 1000))


print( "Paino nykyajan mitoissa: " + str(kilotulos) + " kilogrammaa ja " + str(grammatulos) + " grammaa")
