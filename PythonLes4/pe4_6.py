lijst = ['a', 'b', 'c']
print(lijst)

def wijzig(letterlijst):
    ''''Leegt de lijst en voert vervolgens nieuwe waardes toe'''
    letterlijst.clear()
    letterlijst[:] = ['d', 'e', 'f']

wijzig(lijst)
print(lijst)

