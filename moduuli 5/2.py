
lista = []

luku = input("Enter a number: ")

while luku != "":
    lista.append(int(luku))
    luku = (input("Enter a number: "))

lista.sort(reverse=True)
print(lista[0:5])