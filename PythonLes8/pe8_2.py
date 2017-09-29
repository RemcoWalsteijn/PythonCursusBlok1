import random

def monopolyworp():
    dubbelgegooid = 0
    dob1 = random.randint(1, 6)
    dob2 = random.randint(1, 6)

    while dob1 == dob2:
         totaal = dob1 + dob2
         dubbelgegooid += 1
         if dubbelgegooid < 3:
            print(dob1, '+', dob2, '=', totaal, '(dubbel)')
            dob1 = random.randint(1, 6)
            dob2 = random.randint(1, 6)
            continue
         else:
            print(dob1, '+', dob2, '=', totaal, '(direct naar de gevangenis)')
            break

    else:
        totaal = dob1 + dob2
        print(dob1, '+', dob2, '=', totaal)

monopolyworp()