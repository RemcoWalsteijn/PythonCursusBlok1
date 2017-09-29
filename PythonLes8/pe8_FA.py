stations = ['Schagen', 'Heerhugowaard','Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):
    beginstationreis = input('Vul het beginstation in van je reis: ')
    while beginstationreis not in stations:
        print('Het opgegeven beginstation komt niet voor in het traject van Schagen-Maastrischt, vul alstublieft een beginstation in vanuit dit traject!')
        beginstationreis = input('Vul het beginstation in van je reis: ')
        continue
    else:
        return (beginstationreis)

beginstation = inlezen_beginstation(stations)

def inlezen_eindstation(stations, beginstation):
    eindstation = input('Vul het eindstation in van je reis: ')
    while True:
        if eindstation in stations:
            if stations.index(beginstation) >= stations.index(eindstation):
                print('Het opgegeven eindstation komt eerder voor in het traject dan het opgegeven beginstation, vul alstublieft een geldig eindstation in m.b.t. het opgegeven beginstation!')
                eindstation = input('Vul het eindstation in van je reis: ')
                continue
            else:
                return(eindstation)

        else:
            print('Het opgegeven eindstation komt niet voor in het traject van Schaken-Maastricht')
            eindstation = input('Vul het eindstation in van je reis: ')
            continue

eindstation = inlezen_eindstation(stations, beginstation)

def omroepen_reis(stations, beginstation, eindstation):
    beginstationrangnr = stations.index(beginstation) + 1
    eindstationrangnr = stations.index(eindstation) + 1
    afstand = eindstationrangnr - beginstationrangnr
    ritprijs = afstand * 5
    tussenhalteslijst = stations[beginstationrangnr:eindstationrangnr-1]
    tussenhaltes = ', '.join(map(str, tussenhalteslijst))
    print()
    print('Het beginstation', beginstation, 'is het', str(beginstationrangnr) + 'e station in het traject.')
    print('Het eindstation', eindstation, 'is het', str(eindstationrangnr) + 'e station in het traject')
    print('De afstand bedraagt', afstand, 'station(s)')
    print('De prijs van het kaartje is', ritprijs, 'euro.')
    print('Jij stapt op de trein in:', beginstation)
    print('De tussenhaltes zijn:', tussenhaltes)
    print('Jij stapt uit in:', eindstation)

omroepen_reis(stations, beginstation, eindstation)

