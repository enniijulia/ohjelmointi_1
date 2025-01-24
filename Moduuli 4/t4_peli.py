import random
peliluku = random.randint(1,10)

luku = int(input("arvaa luku numeroiden 1-10 väliltä: "))
while luku!=peliluku:
    if luku<peliluku:
        print("Liian pieni arvaus!")
        luku = int(input("arvaa luku numeroiden 1-10 väliltä: "))
    elif luku>peliluku:
        print("Liian suuri arvaus!")
        luku = int(input("arvaa luku numeroiden 1-10 väliltä: "))

else:
    print("Oikein!")