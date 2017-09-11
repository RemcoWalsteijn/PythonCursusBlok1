Leeftijd = int(input('Geef je leeftijd:'))
Paspoort = input('Heb je een Nederlands paspoort?')

if Leeftijd >= 18 and Paspoort == 'ja' or Leeftijd >= 18 and Paspoort == 'Ja':
    print('Gefeliciteerd, je mag stemmen!')

else:
    print('Je mag helaas niet stemmen!')
