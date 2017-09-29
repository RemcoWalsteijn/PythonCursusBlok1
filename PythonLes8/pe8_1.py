bruin = {'Boxtel', 'Best', 'Breukenlaan', 'Eindhoven', 'Helmond t\' Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Breukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

zelfdelijnen = bruin.intersection(groen)
print('De bruine en groene trajecten lopen beide langs de volgende lijnen:', zelfdelijnen)
print()

uniekebruinelijnen= bruin.difference(groen)
print('De volgende lijnen lopen alleen langs het bruine traject:', uniekebruinelijnen)
print()

allelijnen = bruin.union(groen)
print('Alle lijnen van de trajecten (groen en bruin) zijn:', allelijnen)
