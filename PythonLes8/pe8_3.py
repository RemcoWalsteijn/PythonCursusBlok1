def code(invoerstring):
    for letter in invoerstring:
        rangordenr = ord(letter)
        rangordenr += 3
        eindresultaat = chr(rangordenr)
        print(eindresultaat,end='')

code('RutteAlkmaarDen Helder')