import mysql.connector

def lentokenttä(maakoodi):
    sql = f"SELECT type,count(*) FROM airport WHERE iso_country ='{maakoodi}' group by type desc"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        print(f"maakoodin mukaiset lentokentät: ")
        for rivi in tulos:
            print("  ")
            print(rivi)

    else:
        print("maakoodilla ei löytynyt lentokenttiä.")
        return

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='python',
         password='py123',
         autocommit=True
         )

maakoodi = input("anna maakoodi: ")
lentokenttä(maakoodi)
