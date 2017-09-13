def kwadraten_som(grondgetallen):
    ''''Telt alleen positieve gegeven getallen bij elkaar op'''
    return sum([getal for getal in grondgetallen if getal > 0])

print(kwadraten_som([1, 5, -5]))