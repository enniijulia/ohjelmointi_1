luku = int(input("anna kokonaisluku: "))

if luku<2:
    print("luku ei ole alkuluku.")

else:
    onko_alkuluku = True
    for i in range(2,int(luku ** 0.5) + 1):
        if luku % i == 0:
            onko_alkuluku = False
            break

    if onko_alkuluku:
        print("luku on alkuluku!")
    else:
        print("luku ei ole alkuluku!")

