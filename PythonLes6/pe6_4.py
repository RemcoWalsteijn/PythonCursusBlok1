from itertools import chain

studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    gemiddeldelijst = []
    for cijfers in studentencijfers:
        gemiddeldeleerling = sum(cijfers) / 3
        gemiddeldelijst.append(gemiddeldeleerling)
    return(gemiddeldelijst)

def gemiddelde_van_alle_studenten(studentencijfers):
    allecijfers = list(chain.from_iterable(studentencijfers))
    totalecijfer = sum(allecijfers) / len(studentencijfers)
    return(totalecijfer)

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
