invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
lijst = invoer.split('-')

getallenlijst = list(map(int, lijst))
getallenlijstmax = max(getallenlijst)
getallenlijstmin = min(getallenlijst)
getallenlijstlengte = len(getallenlijst)
getallenlijsttotaal = sum(getallenlijst)
getallenlijstgemiddelde = getallenlijsttotaal / getallenlijstlengte

print('Gesorteerte list van ints: ' + str(sorted(getallenlijst)))
print('Grootste getal: ' + str(getallenlijstmax) + ' en Kleinste getal: ' + str(getallenlijstmin))
print('Aantal getallen: ' + str(getallenlijstlengte) + ' en Som van de getallen: ' + str(getallenlijsttotaal))
print('Gemiddelde: ' + str(getallenlijstgemiddelde))

