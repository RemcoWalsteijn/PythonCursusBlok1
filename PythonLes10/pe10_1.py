import xmltodict

with open('producten.xml') as xml:
    dict = xmltodict.parse(xml.read())

namen = []
for naam in dict['Artikelen']['Rij']:
    namen.append(naam['Naam'])

print('Dit zijn alle artikelnamen uit het XML bestand: \n')
for naam in namen:
    print(naam)