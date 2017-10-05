import random

print('1: Ik wil weten hoeveel kluizen er nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')
print('4: Ik geef mijn kluis terug' + '\n')
keuze = input('Kies één van de opties d.m.v. het nummer in te voeren van de optie: ')


def toon_aantal_kluizen_vrij():
    with open('kluizen.txt') as kluizen:
        bezet = len(list(kluizen))
        vrij = 12 - bezet
        print('Er zijn ' + str(vrij) + ' kluizen vrij!')

def nieuwe_kluis():
    with open('kluizen.txt') as kluizen:
            readlines = kluizen.read()
            content = readlines.splitlines()
            kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for kluis in content:
            if kluis != '':
                   kluizen = open('kluizen.txt', 'a')
                   kluis = kluis.split(";")
                   kluisnummer = int(kluis[0])
                   kluisnummers.remove(kluisnummer)
    if len(kluisnummers) != 0:
            ww = input("Vul een wachtwoord in voor je kluis: ")
            welkekluis = random.choice(kluisnummers)
            kluizen.write(str(welkekluis) + ';' + ww + '\n')
            print('Je kluis is kluisnummer: ' + str(welkekluis))
            kluizen.close()
    if len(kluisnummers) <= 0:
            print('Er zijn helaas geen kluizen beschikbaar')

def open_kluis():
        kluisnummer = input('Vul je kluisnummer in: ')
        ww = input('Vul het wachtwoord in van je kluisje: ')
        combinatie = (kluisnummer + ';' + ww)
        with open('kluizen.txt') as kluizen:
            readlines = kluizen.read()
            content = readlines.splitlines()
            if combinatie in content:
                print('Je kluisje is geopend!')

            else:
                print('De combinatie van het opgegeven kluisnummer + wachtwoord is ongeldig')

if keuze == '1':
    toon_aantal_kluizen_vrij()

if keuze == '2':
    nieuwe_kluis()

if keuze == '3':
    open_kluis()


