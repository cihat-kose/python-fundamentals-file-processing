"""
Oppgave 1.5
Utvid Oppgave 1.3 slik at brukeren kan angi et intervall [m, n] i stedet for 1-10,
og programmet skriver ut en pent formatert tabell for tallet i hele intervallet.

Eksempel på tabell:

| 1 | 2 | 3 |
|---|---|---|
| 1 | 2 | 3 |
| 2 | 4 | 6 |
| 3 | 6 | 9 |
"""

# # Oppgave 1.3
# tall = int(input("Skriv inn et tall: "))
#
# for i in range(1, 11):
#     print(f"{tall} * {i} = {tall * i}")

# Oppgave 1.5
startverdi = int(input("Skriv inn startverdi (m): "))
sluttverdi = int(input("Skriv inn sluttverdi (n): "))

celle_bredde = 3

overskrift = "| " + " | ".join(f"{i:>{celle_bredde}}" for i in range(startverdi, sluttverdi + 1)) + " |"
separator = "| " + " | ".join("-" * celle_bredde for _ in range(startverdi, sluttverdi + 1)) + " |"
print(overskrift)
print(separator)

for i in range(startverdi, sluttverdi + 1):
    rad = "| " + " | ".join(f"{i * j:>{celle_bredde}}" for j in range(startverdi, sluttverdi + 1)) + " |"
    print(rad)
