nimi_lista = []
while True:
    nimet = input("anna nimi tai paina ENTER lopettaaksesi: ")
    if nimet == "":
        break

    if nimet in nimi_lista:
        print("aiemmin syötetty nimi!")
    else:
        print("uusi nimi!")
        nimi_lista.append(nimet)

for nimet in nimi_lista:
    print(nimet)