infile = open('kaartnummers.txt', 'r')
for line in infile:
        line = line.strip()
        f1 = line.split(',')
        print(f1[1],'heeft kaartnummer:',f1[0])
infile.close()