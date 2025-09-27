"""
Oppgave 1.1
Lag et program som ber brukeren om å skrive inn et positivt heltall (int)
og finner summen av alle tall fra 1 til dette tallet (inkludert).
Summen skal beregnes ved hjelp av en for-løkke.
"""

tall = int(input("Skriv inn et positivt heltall: "))

total = 0

for i in range(1, tall + 1):
    total += i

print(f"Summen av tallene fra 1 til {tall} (inkludert) er: {total}")
