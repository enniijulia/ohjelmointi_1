def main():
    airports = {}

    while True:
        print("\nValitse toiminto:")
        print("1 - Syötä uusi lentoasema")
        print("2 - Hae lentoaseman tiedot")
        print("3 - Lopeta")

        valinta = input("Valintasi: ")

        if valinta == "1":
            icao = input("Syötä lentoaseman ICAO-koodi: ").strip().upper()
            name = input("Syötä lentoaseman nimi: ").strip()
            airports[icao] = name
            print("Lentoasema tallennettu.")

        elif valinta == "2":
            icao = input("Syötä lentoaseman ICAO-koodi: ").strip().upper()
            if icao in airports:
                print(f"Lentoasema: {airports[icao]}")
            else:
                print("Lentoasemaa ei löytynyt.")

        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break

        else:
            print("Virheellinen valinta, yritä uudelleen.")


if __name__ == "__main__":
    main()


