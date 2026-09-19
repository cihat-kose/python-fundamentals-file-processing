"""
Oppgave 1.4
Lag et program som bytter plass på to elementer i en gitt liste.
Programmet skal ta utgangspunkt i følgende liste:

fruits = ["eple", "banan", "appelsin", "drue", "kiwi"]

1. Be brukeren om å skrive inn to indekser (input) som angir hvilke
   elementer i listen som skal bytte plass
2. Bytt plass på elementene som ligger på de angitte indeksene
3. Skriv ut den oppdaterte listen

Hvis en eller begge indeksene er ugyldige (ikke i listen),
skal programmet gi en passende feilmelding.
"""

frukt = ["eple", "banan", "appelsin", "drue", "kiwi"]

try:
    første_indeks = int(input("Skriv inn første indeks: "))
    andre_indeks = int(input("Skriv inn andre indeks: "))

    if 0 <= første_indeks < len(frukt) and 0 <= andre_indeks < len(frukt):
        frukt[første_indeks], frukt[andre_indeks] = frukt[andre_indeks], frukt[første_indeks]
        print(f"Opdatert liste: {frukt}")
    else:
        print("Ugyldig indeks!")

except ValueError:
    print("Du må skrive tall!")
