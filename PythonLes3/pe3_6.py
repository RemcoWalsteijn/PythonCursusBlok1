s = 'Guido van Rossum heeft programmeertaal Python bedacht.'

for klinkers in s:
    if klinkers in 'aeoiuAEIOU':
        print(klinkers)