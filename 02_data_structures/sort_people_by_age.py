"""
Oppgave 2.4
Skriv et program som sorterer denne dictionary etter alder
hvor den eldste skal være først. Skriv ut resultatet.
"""

# Oppgave 2.3
# navn_og_alder_liste = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
#
# navn_alder_dict = {navn_og_alder_liste[i]: navn_og_alder_liste[i+1] for i in range(0, len(navn_og_alder_liste), 2)}
#
# for navn, alder in navn_alder_dict.items():
#     print(f"{navn} er {alder} år")

navn_og_alder_liste = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

navn_alder_dict = {}

for i in range(0, len(navn_og_alder_liste), 2):
    navn_alder_dict[navn_og_alder_liste[i]] = navn_og_alder_liste[i + 1]

sorted_navn = sorted(navn_alder_dict, key=navn_alder_dict.get, reverse=True)

for i in sorted_navn:
    print(f"{i} er {navn_alder_dict[i]} år")
