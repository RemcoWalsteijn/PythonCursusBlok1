lijst = eval(input('Geef een lijst met minimaal 10 strings: '))
nieuwelijst = []
for string in lijst:
    if len(string) == 4:
        nieuwelijst.append(string)

print('De nieuw-gemaakte lijst met alle vier-letter strings is: ' + str(nieuwelijst))