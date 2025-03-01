komento = input ("Anna komento: ")
while komento!="lopeta":
    if komento=="MAYDAY":
        break
    print ("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
else:
    print ("Näkemiin.")
print ("Toiminnot lopetettu.")


#Ohjelma tulostaa Näkemiin-tekstin yhden kerran silloin, kun toistorakenteesta poistutaan normaalisti alkuehdon tullessa epätodeksi:

#Anna komento: tanssi
#Suoritan toiminnon: tanssi
#Anna komento: lopeta
#Näkemiin.
#Toiminnot lopetettu.



#Kun ohjelmasta poistutaan break-lauseella, tekstiä ei tulosteta:

#Anna komento: tanssi
#Suoritan toiminnon: tanssi
#Anna komento: MAYDAY
#Toiminnot lopetettu.