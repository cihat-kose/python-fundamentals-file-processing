"""
Oppgave 1.3
Lag et program som ber brukeren skrive inn et tall og genererer multiplikasjonstabellen
for dette tallet (fra 1 til 10). Eksempel:
Input: 3
Output:
3 * 1
3 * 2
3 * 3
Osv..
"""

tall = int(input("Skriv inn et tall: "))

for i in range(1, 11):
    print(f"{tall} * {i} = {tall * i}")
