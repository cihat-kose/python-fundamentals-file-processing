"""
Oppgave 5.1
Skriv et program som summerer opp antall dager lånene ble forlenget og skriv ut svaret.
"""

import csv


def summer_forlengelser(filnavn):
    total = 0
    with open(filnavn, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for rad in reader:
            verdi = rad.get("Forlenget", "").strip()
            if verdi.isdigit():
                total += int(verdi)
            elif verdi:
                print(f"Ugyldig verdi: {verdi}")
    return total


if __name__ == "__main__":
    resultat = summer_forlengelser("bokutlån.csv")
    print(f"Totalt antall dager lånene ble forlenget: {resultat}")
