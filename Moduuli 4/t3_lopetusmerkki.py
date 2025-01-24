numbers = []
luku = 0
while luku!="":
    luku = input("syötä jokin luku TAI tyhjä merkkijono lopettaaksesi: ")
    if luku == "":
        break
    number = float(luku)
    numbers.append(number)
if numbers:
    pienin = min(numbers)
    suurin = max(numbers)
    print(f"pienin luku syötetyistä luvuista: {pienin:.0f}")
    print(f"suurin luku syötetyistä luvuistaa: {suurin:.0f}")







