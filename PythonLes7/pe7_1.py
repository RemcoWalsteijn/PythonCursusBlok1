getal = int(input('Geef een getal: '))
aantalkeer = 0
totaalgetal = getal

while getal != 0:
    getal = int(input('Geef een getal: '))
    totaalgetal += getal
    aantalkeer += 1

print('Er zijn ' + str(aantalkeer) + ' getallen ingevoerd, de som is: ' + str(totaalgetal))


