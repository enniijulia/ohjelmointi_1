import math

def laske_yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * (sade / 100) ** 2
    return hinta / pinta_ala

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))

yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta: {yksikkohinta2:.2f} €/m²")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza on parempi vastine rahalle.")
elif yksikkohinta1 > yksikkohinta2:
    print("Toinen pizza on parempi vastine rahalle.")
else:
    print("Molemmilla pizzoilla on sama yksikköhinta.")
