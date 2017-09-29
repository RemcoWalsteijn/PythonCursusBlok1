infile = open("kaartnummers.txt", 'r')

intList = [int(x.split(",")[0]) for x in infile.readlines()]
regels = len(intList)
number = max(intList)
laatsteregel = str(intList.index(max(intList)) + 1)

string_format = 'Deze file telt {0} regels\n' \
                'Het grootste kaartnummer is: {1} en dat staat op regel {2}'
result = string_format.format(regels, number, laatsteregel)
print(result)

infile.close()