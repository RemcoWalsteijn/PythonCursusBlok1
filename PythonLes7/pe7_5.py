klas = {}


def namen():
    '''''de gebruiker voert steeds een naam in d.m.v. de while loop. De namen en het aantal keer dat ze zijn ingevuld worden toegevoegd aan de klas dictionary'''
    naam = input('Vul de naam in van een student uit de klas: ')
    while naam != '':
        if naam not in klas: #Wanneer de naam nog niet eerder is ingevuld dan:
            klas[naam] = 1          #De naam is 1 keer ingevuld en krijgt de waarde 1

        else:                       #Wanneer de naam al eens eerder is ingevuld dan:
            klas[naam] += 1         #De naam is opnieuw ingevuld dus bij de waarde van de naam wordt er 1 bijgeteld.
        naam = input('Volgende naam: ')
        continue
namen()

#Ik heb hieronder twee for loops gebruikt om te zorgen dat de eerste loop altijd als eerst geprint wordt (zoals in het voorbeeld plaatje stond). Bij een if/else was de output ongesorteerd.
for k, v in klas.items():
    if v == 1:
        print('Er is 1 student met de naam', k)

for k, v in klas.items():
    if v > 1:
        print('Er zijn', v, 'studenten met de naam', k)
