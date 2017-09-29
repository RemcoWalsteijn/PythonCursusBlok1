def gemiddelde():
    willekeurigezin = input('Vul alstublieft een willekeurige zin in: ')
    woorden = willekeurigezin.split()
    gemiddeld = sum(len(woord) for woord in woorden) / len(woorden)
    print(gemiddeld)

gemiddelde()