import xmltodict

with open('stations.xml') as xml:
    dict = xmltodict.parse(xml.read())

station_codes_types = []
station_codes_synoniemen = []
station_codes_langenamen = []

for stations in dict['Stations']['Station']:
    station_codes_types.append([stations['Code'],stations['Type']])

for stations in dict['Stations']['Station']:
    station_codes_synoniemen.append([stations['Code'],stations['Synoniemen']])

for stations in dict['Stations']['Station']:
    station_codes_langenamen.append([stations['Code'],stations['Namen']['Lang']])

print('Dit zijn de codes en types van de 4 stations:')
for codes,types in station_codes_types:
    print('{:<4} - {}'.format(codes,types))
print()

print('Dit zijn alle stations met één of meer synoniemen:')
for codes, synoniemen in station_codes_synoniemen:
    if synoniemen != None:
        synoniemen = ', '.join(synoniemen['Synoniem'])
        print('{:<4} - {}'.format(codes,synoniemen))
print()

print('Dit is de lange naam van elk station:')
for codes, langenamen in station_codes_langenamen:
    print('{:<4} - {}'.format(codes, langenamen))
