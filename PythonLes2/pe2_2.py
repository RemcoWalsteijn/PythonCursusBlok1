cijferICOR = 7
cijferPROG = 7
cijferCSN = 8

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning = (cijferICOR * 30) + (cijferPROG * 30) + (cijferCSN * 30)
overzicht = 'Mijn cijfers (gemiddeld een ' + (str(gemiddelde)) + ' leveren een beloning van €' + (str(beloning)) + ' op!'
print(overzicht)