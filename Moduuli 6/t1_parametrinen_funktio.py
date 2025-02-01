import random
noppa = 0
def noppa():
    return random.randint(1,6)

print("Heitetään noppaa, kunnes saadaan kutonen.")
while True:
    silmaluku = noppa()
    print(f"Nopan silmäluku: {silmaluku}")
    if silmaluku == 6:
        break