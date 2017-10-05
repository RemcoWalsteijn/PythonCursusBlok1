import datetime
import csv

naam = input("Wat is je achternaam? ")

while naam != 'einde':
    datum_tijd = datetime.datetime.now().strftime('%a %d %b %Y at %H:%M')
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    gegevens = (datum_tijd,naam,voorl,gbdatum,email)
    with open('inloggers.csv', 'a', newline='') as bestand:
        writer = csv.writer(bestand, delimiter=';')
        writer.writerow(gegevens)
    naam = input("Wat is je achternaam? ")