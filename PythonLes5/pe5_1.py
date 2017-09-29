def convert(Celsius):
        Fahrenheit = (Celsius * 1.8) + 32
        return(Fahrenheit)

def table(Celsius):
    print('{:>5} {:>10}'.format('F', 'C'))
    for graden in Celsius:
        Fahrenheit = convert(graden)
        print('{:>5} {:>10}'.format(Fahrenheit, graden))

Celsius = list(range(-30, 50, 10))

table(Celsius)



