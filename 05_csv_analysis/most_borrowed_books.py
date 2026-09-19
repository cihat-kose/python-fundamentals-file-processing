"""
Oppgave 5.5
Skriv en funksjon som finner hvilke bøker som har blitt lånt flest ganger.
Funksjonen skal returnere en oversikt over boktitlene og antallet ganger de har blitt lånt ut.
Hvis flere bøker har blitt lånt ut like mange ganger, skal de sorteres alfabetisk. Skriv ut svaret.

Türkçe
En çok kaç kez ödünç alınan kitap(ları) bulan bir fonksiyon yaz.
Fonksiyon, kitap başlıkları ve kaç kere ödünç alındıklarının dökümünü döndürmeli.
Eğer birden fazla kitap aynı sayıda ödünç alınmışsa alfabetik olarak sıralanmalı. Sonucu yazdır.
"""

import csv
from collections import Counter


def mest_lånte_bøker(filnavn):
    teller = Counter()
    with open(filnavn, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for rad in reader:
            bok = (rad.get("Boktittel") or "").strip()
            if bok:
                teller[bok] += 1

    if not teller:
        return []

    maks = max(teller.values())

    mest = [(tittel, antall) for tittel, antall in teller.items() if antall == maks]

    def alfabetisk(element):
        return element[0]

    mest.sort(key=alfabetisk)

    return mest


if __name__ == "__main__":
    resultater = mest_lånte_bøker("library_loans.csv")
    print("Mest utlånte bøker:")
    for tittel, antall in resultater:
        print(f"- {tittel} ({antall} ganger)")
