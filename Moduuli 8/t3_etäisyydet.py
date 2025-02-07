import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='python',
    password='py123',
    autocommit=True
)

def lentokenttä_koordinaatit(icao1, icao2):
    sql = f"SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident IN ('{icao1}', '{icao2}')"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if len(tulos) < 2:
        print("ei tulosta: tarkista syöttämäsi ICAO-koodit")
        return

    kenttä1 = (tulos[0][0], (tulos[0][1], tulos[0][2]))
    kenttä2 = (tulos[1][0], (tulos[1][1], tulos[1][2]))

    print("\nEnsimmäinen ICAO-koodi kuuluu kentälle:", kenttä1[0])
    print("Toinen ICAO-koodi kuuluu kentälle:", kenttä2[0])

    etaisyys = distance.distance(kenttä1[1], kenttä2[1]).km
    print(f"\nNäiden kahden lentokentän välinen etäisyys on: {etaisyys:.0f} km.")

eka = input("Syötä ensimmäinen ICAO-koodi: ").strip().upper()
toka = input("Syötä toinen ICAO-koodi: ").strip().upper()
lentokenttä_koordinaatit(eka, toka)





