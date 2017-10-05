import csv

with open('scores.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    antwoord = max(reader, key=lambda regel: int(regel[2].replace(';', '')))
print('De hoogste score is: {} op {} behaald door {}'.format(antwoord[2],antwoord[1],antwoord[0]))