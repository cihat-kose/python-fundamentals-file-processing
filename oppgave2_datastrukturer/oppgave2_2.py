"""
Oppgave 2.2
Ta utgangspunkt i en liste der tekst og tall er plassert parvis med navn og alder slik:

["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
"""

navn_og_alder_liste = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

navnliste = [navn_og_alder_liste[i] for i in range(0, len(navn_og_alder_liste), 2)]
aldersliste = [navn_og_alder_liste[i] for i in range(1, len(navn_og_alder_liste), 2)]

print("Navn:", navnliste)
print("Alder:", aldersliste)
