tuumat_cm = 2.54
tuumat = int(input("anna tuumat: "))
while tuumat>0:
    if tuumat < 0:
        break
    print(f"antamasi tuumat muutettuna senttimetreiksi: {tuumat*tuumat_cm:.2f}")
    tuumat = int(input("anna tuumat: "))
else:
    print("toiminta lopetettu")




