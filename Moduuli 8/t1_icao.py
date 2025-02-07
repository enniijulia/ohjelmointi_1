import mysql.connector

def airport_name(icao):
    sql = f'SELECT name from airport where ident = "{icao}"'

    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"lentokentän nimi {rivi[0]}")
    else:
        print("lentokenttää ei löytynyt.")
    return

# Pääohjelma
yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='python',
         password='py123',
         autocommit=True
         )

lentokenttä = input("Anna ICAO: ")
airport_name(lentokenttä)











