try:
    aantalpersonen = int(input('Hoeveel personen gaan er mee op reis? '))
    if aantalpersonen < 0:
        print('Gebruik cijfers voor het invoeren van het aantal!')
    else:
        kostenperpersoon = 4356.0 / aantalpersonen
        print('De kosten per persoon voor het hotel zijn: €', kostenperpersoon)
except ZeroDivisionError:
    print('Delen door 0 kan niet!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer!')
