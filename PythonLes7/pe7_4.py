dict = {}

def ticker(filename):
    with open(filename) as file:
        for line in file: #voor elke lijn in filename
            (key, val) = line.rstrip('\n').split(':') #haalt de line breaks weg en split de lijnen op het : teken
            dict[key] = val #voegt de keys met waardes toe aan de dictionary
        return(dict)

ticker('tickersymbolen.txt')

bedrijfsnaam = input('Enter Company name: ')
for k, v in dict.items(): #voor elke key, waarde uit de dictionary
    if bedrijfsnaam == k:
        print('Ticker symbol:', v)
        print()

tickersymbool = input('Enter Ticker symbol: ')
for k, v in dict.items(): #voor elke key, waarde uit de dictionary
    if tickersymbool == v:
        print('Company name:', k)