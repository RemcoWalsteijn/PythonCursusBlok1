def standaardprijs(afstandKM):
    ''''De standaardprijs wordt berekent aan de hand van het aantal KM. Wanneer er 0KM wordt gereisd is de standaardprijs 0'''
    if afstandKM > 50.0:
        totaalbedrag = 15 + (afstandKM * 0.6)
        return(totaalbedrag)

    if afstandKM == 0.0:
        return(afstandKM)

    else:
        totaalbedrag = 15 + (afstandKM * 0.8)
        return(totaalbedrag)

def ritprijs(leeftijd, weekendrit, afstandKM):
    ''''De ritprijs wordt berekend aan de hand van de functie standaardprijs. Er wordt rekening gehouden met 3 meegegeven parameters'''
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

print(ritprijs(11, False, 1.0))
