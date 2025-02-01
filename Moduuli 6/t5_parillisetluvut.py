def vain_parilliset(numerot):
    return [luku for luku in numerot if luku % 2 == 0]

numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parilliset = vain_parilliset(numerot)

print(f"Alkuperäinen lista: {numerot}")
print(f"Parilliset luvut: {parilliset}")
