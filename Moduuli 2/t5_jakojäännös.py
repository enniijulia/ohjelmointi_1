luoti = 13.3
naula = luoti * 32
leiviska = 20 * naula

A = int(input("anna leiviskät: "))
B = int(input("anna naulat: "))
C = int(input("anna luodit: "))

A1 = A * leiviska
B1 = B * naula
C1 = C * luoti

paino = A1 + B1 + C1

kg = paino/1000
g = paino%1000

print(f"paino on: {kg:.0f}" " kg " f"{g:.1f}" " g")




















