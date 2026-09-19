"""
Oppgave 5.2
Lag en funksjon som beregner hvor mange bøker som er lånt ut per sjanger
(f.eks. "Fantasy: 3, Krim: 5", osv.) og skriv ut svaret.
"""

import csv
from collections import Counter


def bøker_per_sjanger(filnavn):
    gyldige_sjangre = {"Fiksjon", "Krim", "Sakprosa", "Fantasy"}
    teller = Counter()

    with open(filnavn, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for rad in reader:
            sjanger = rad.get("Sjanger", "").strip()
            if sjanger in gyldige_sjangre:
                teller[sjanger] += 1
            elif sjanger:
                print(f"Ugyldig sjanger funnet: {sjanger}")

    return teller


if __name__ == "__main__":
    resultat = bøker_per_sjanger("library_loans.csv")
    for sjanger, antall in resultat.items():
        print(f"{sjanger}: {antall}")
