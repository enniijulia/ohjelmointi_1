sukupuoli = input("Mikä on biologinen sukupuolesi? ")

hemoglobiini = int(input("Anna hemoglobiiniarvosi: "))

if sukupuoli=="nainen" and 0<=hemoglobiini<117:
    print("hemoglobiini on alhainen.")
if sukupuoli=="nainen" and 117<=hemoglobiini<=175:
    print("hemoglobiini on normaali.")
if sukupuoli=="nainen" and 175<hemoglobiini<300:
    print("hemoglobiini on korkea.")

if sukupuoli=="mies" and 0<=hemoglobiini<134:
    print("hemoglobiini on alhainen.")
if sukupuoli=="mies" and 134<=hemoglobiini<=195:
    print("hemoglobiini on normaali.")
if sukupuoli=="mies" and 195<hemoglobiini<300:
    print("hemoglobiini on korkea.")






