"""
Oppgave 5.4
Lag en funksjon som lister opp alle bøkene som ikke ble levert tilbake.
Returner en liste med navnene på bøkene og hvem som lånte dem, og skriv ut svaret.
"""

import csv


def ikke_levert_bøker(filnavn):
    resultat = []

    with open(filnavn, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for rad in reader:
            tilbake = (rad.get("Tilbakelevert") or "").strip().lower()
            if tilbake == "nei":
                fornavn = rad.get("Fornavn", "").strip()
                etternavn = rad.get("Etternavn", "").strip()
                bok = rad.get("Boktittel", "").strip()
                resultat.append((bok, f"{fornavn} {etternavn}"))

    return resultat


if __name__ == "__main__":
    bøker = ikke_levert_bøker("bokutlån.csv")
    if not bøker:
        print("Alle bøker er levert tilbake.")
    else:
        print("Bøker som ikke ble levert tilbake:")
        for bok, navn in bøker:
            print(f"- {bok} (lånt av {navn})")
