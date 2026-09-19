"""
Oppgave 5.3
Beregn den gjennomsnittlige låneperioden i antall hele dager for alle bøker som er lånt ut,
inkludert forlengelsene, og skriv ut svaret.

Türkçe
Tüm kitaplar için ortalama ödünç süresini (tam gün cinsinden) hesapla;
uzatmaları (forlenget) da dahil et ve sonucu yazdır.
"""

import csv


def gjennomsnittlig_låneperiode(filnavn):
    total_dager = 0
    antall = 0

    with open(filnavn, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, rad in enumerate(reader, start=2):
            lp = (rad.get("Låneperiode") or "").strip()
            ext = (rad.get("Forlenget") or "").strip()

            if lp == "" or ext == "":
                continue

            try:
                lp_i = int(lp)
                ext_i = int(ext)
                if lp_i < 0 or ext_i < 0:
                    raise ValueError("negativ verdi")
                total_dager += lp_i + ext_i
                antall += 1
            except Exception:
                print(f"Ugyldig verdi i rad {i}: Låneperiode={lp!r}, Forlenget={ext!r}")

    if antall == 0:
        print("Ingen gyldige rader å beregne gjennomsnitt fra.")
        return None

    snitt = round(total_dager // antall)
    print(f"Gjennomsnittlig låneperiode (inkl. forlengelser): {snitt} dager")
    return snitt


if __name__ == "__main__":
    gjennomsnittlig_låneperiode("library_loans.csv")
