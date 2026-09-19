"""
Oppgave 2.5
Ta utgangspunkt i dictionary som er sortert på navn i Oppgave 2.4
og lag en ny liste med disse verdiene slik at listen får samme format
som den i Oppgave 2.2, men sortert på navn.

["Anna", 25, "Bjørn", 30, "Cecilie", 28, "Tor", 24]
"""

# Oppgave 2.4
# navn_og_alder_liste = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
#
# navn_alder_dict = {}
#
# for i in range(0, len(navn_og_alder_liste), 2):
#     navn_alder_dict[navn_og_alder_liste[i]] = navn_og_alder_liste[i+1]
#
# sorted_navn = sorted(navn_alder_dict, key=navn_alder_dict.get, reverse=True)
#
# for i in sorted_navn:
#     print(f"{i} er {navn_alder_dict[i]} år")

navn_og_alder_liste = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

navn_alder_dict = {}
for i in range(0, len(navn_og_alder_liste), 2):
    navn_alder_dict[navn_og_alder_liste[i]] = navn_og_alder_liste[i + 1]

sorted_navn = sorted(navn_alder_dict.keys())

sorted_list = []
for navn in sorted_navn:
    sorted_list.append(navn)
    sorted_list.append(navn_alder_dict[navn])

print(sorted_list)
