string = input('Geef een string van vier letters: ')

while len(string) != 4:
    print(string, 'heeft', len(string), 'letters')
    string = input('Geef een string van vier letters: ')
    if len(string) == 4:
        break

print('Inlezen van correcte string:', string, 'is geslaagd')