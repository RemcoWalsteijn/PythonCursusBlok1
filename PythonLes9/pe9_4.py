import csv

with open('producten.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)
    duursteregel = max(data, key=lambda x: float(x[4]))
    minstevoorraad = min(data, key=lambda x: int(x[3]))
    voorraadcijfers = []
    for x in data:
        voorraadcijfers.append(int(x[3]))
    totalevoorraad = sum(voorraadcijfers)

print('Het duurste artikel is {} en die kost {} Euro'.format(duursteregel[2],duursteregel[4]))
print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(minstevoorraad[3],minstevoorraad[0]))
print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totalevoorraad))