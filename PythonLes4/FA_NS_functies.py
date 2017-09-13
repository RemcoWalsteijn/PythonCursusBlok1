def standaardprijs(afstandKM):
    if afstandKM > 50.0:
        totaalbedrag = 15 + (afstandKM * 0.6)
        return(totaalbedrag)
    else:
        totaalbedrag = 15 + (afstandKM * 0.8)
        return(totaalbedrag)

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardkostenKM = standaardprijs(afstandKM)

    if weekendrit == True:
        if leeftijd >= 65 or leeftijd < 12:
            kortingsprijs = standaardkostenKM * 0.65
            return(kortingsprijs)
        else:
            kortingsprijs = standaardkostenKM * 0.6
            return(kortingsprijs)

    else:
        if leeftijd >= 65 or leeftijd < 12:
            kortingsprijs = standaardkostenKM * 0.7
            return(kortingsprijs)
        else:
            return(standaardkostenKM)

print(ritprijs(11, False, 20.0))
