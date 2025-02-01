import random

tahkot = int(input("anna nopan tahkojen määrä: "))
def noppa(tahkot):
    return random.randint(1, tahkot)


print(f"Heitetään {tahkot}-tahoista noppaa, kunnes saadaan maksimisilmäluku ({tahkot}).")

while True:
    silmäluku = noppa(tahkot)
    print(f"Nopan silmäluku: {silmäluku}")
    if silmäluku == tahkot:
        break