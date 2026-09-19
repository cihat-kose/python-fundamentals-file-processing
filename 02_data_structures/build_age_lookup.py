"""
Oppgave 2.3
Ta utgangspunkt i listene fra Oppgave 2.2 og lag en dictionary
der tekstverdier fra listen med navn blir nøkler
og tallverdiene fra listen med alder blir verdier.
Skriv ut innholdet av denne dictionary på formatet:

"Cecilie er 25 år"
"Bjørn er 30 år"
"""

# Oppgave 2.2
# ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

navn_og_alder_liste = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

navn_alder_dict = {navn_og_alder_liste[i]: navn_og_alder_liste[i + 1] for i in range(0, len(navn_og_alder_liste), 2)}

for navn, alder in navn_alder_dict.items():
    print(f"{navn} er {alder} år")
