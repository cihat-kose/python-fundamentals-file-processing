"""
Oppgave 2.1
Skriv et program som leser inn en dato i formatet “dd/mm/yyyy” fra brukeren.
Programmet skal deretter sjekke om datoen er gyldig.
Hvis datoen er ugyldig, skal programmet skrive en passende feilmelding.
"""

dag, måned, år = map(int, input("Skriv inn en dato (dd/mm/yyyy): ").split('/'))

if 1 <= dag <= 31 and 1 <= måned <= 12 and år > 0:
    if måned in [1, 3, 5, 7, 8, 10, 12] and dag <= 31:
        print("Gyldig dato")
    elif måned in [4, 6, 9, 11] and dag <= 30:
        print("Gyldig dato")
    elif måned == 2 and (dag <= 28 or (dag == 29 and år % 4 == 0 and (år % 100 != 0 or år % 400 == 0))):
        print("Gyldig dato")
    else:
        print("Ugyldig dato")
else:
    print("Ugyldig dato")
