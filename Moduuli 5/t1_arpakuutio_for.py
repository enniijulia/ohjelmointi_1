import random
heitot = []
heitto_lk = int(input("Kuinka monta noppaa haluat heittää? "))
tulos = 0
for n in range(0,heitto_lk):
    noppa = random.randint(1,6)
    heitot.append(noppa)
for n in heitot:
    tulos = tulos + n
print("silmälukujen summa on " + str(tulos))




















#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
#Käytä for-toistorakennetta.