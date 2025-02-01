luvut = []
luku = input("Anna luku tai lopeta painamalla Enter: ")
while luku!="":
    luku2 = int(luku)
    luvut.append(luku2)
    luku = input("Anna luku tai lopeta painamalla Enter: ")


luvut.sort(reverse=True)

for index in range(0,5):
    print (luvut[index])

