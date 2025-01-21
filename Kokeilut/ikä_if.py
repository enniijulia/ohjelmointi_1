age = int(input("anna ikä: "))
if 15<=age<18:
    paino = float(input("anna paino (kg): "))
if age>=18 or age>15 and paino>=55:
    print("lääkkeen käyttö on sallittua.")
else:
    print("lääkkeen käyttö ei ole sallittua.")



