"""
Oppgave 2.6
Konverter datasettet fra Oppgave 2.2 til en liste av dictionaries
med formatet:

{"navn": "Cecilie", "alder": 28}

Oppgave 2.2’deki veri setini şu formata sahip dictionary’lerden oluşan bir listeye dönüştür:

{"navn": "Cecilie", "alder": 28}
"""

# """
# Oppgave 2.2
# Ta utgangspunkt i en liste der tekst og tall er plassert parvis med navn og alder slik:
#
# ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
# """
#
# navn_og_alder_liste = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
#
# navnliste = [navn_og_alder_liste[i] for i in range(0, len(navn_og_alder_liste), 2)]
# aldersliste = [navn_og_alder_liste[i] for i in range(1, len(navn_og_alder_liste), 2)]
#
# print("Navn:", navnliste)
# print("Alder:", aldersliste)

navn_og_alder_liste = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

dictionary_list = []

for i in range(0, len(navn_og_alder_liste), 2):
    navn = navn_og_alder_liste[i]
    alder = navn_og_alder_liste[i + 1]
    dictionary_list.append({"navn": navn, "alder": alder})

print(dictionary_list)
