"""
Oppgave 1.2
Skriv et program som ber brukeren skrive inn to setninger.
Programmet skal deretter sammenligne lengden på de to setningene
og skrive ut hvilken som er lengst og antall karakterer det er i denne setningen.
"""

setning1 = input("Skriv inn første setning: ")
setning2 = input("Skriv inn andre setning: ")

lengde1 = len(setning1)
lengde2 = len(setning2)

if lengde1 > lengde2:
    print(f"Den lengste setningen er \"{setning1}\" og antall karakterer er {lengde1}")
elif lengde2 > lengde1:
    print(f"Den lengste setningen er \"{setning2}\" og antall karakterer er {lengde2}")
else:
    print(f"Begge setningene er like lange og antall karakterer er {lengde1}")
