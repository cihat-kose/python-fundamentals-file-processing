"""
Oppgave 3.2
Lag en funksjon som tar inn to datoer som strenger på formatet “dd/mm/yyyy”
og returnerer antall dager mellom dem.
Hvis den første datoen er senere enn den andre, skal funksjonen fortsatt returnere antall dager (positivt tall).

Eksempel:
Input: "21/11/2024", "01/01/2024" → Output: 325 dager
"""

from datetime import datetime


def antall_dager_mellom_datoer(dato1_str, dato2_str):
    dato_format = "%d/%m/%Y"

    dato1 = datetime.strptime(dato1_str, dato_format)
    dato2 = datetime.strptime(dato2_str, dato_format)

    delta = dato2 - dato1

    return abs(delta.days)


# Test tilfeller
print(antall_dager_mellom_datoer("21/11/2024", "01/01/2024"))  # Output: 325
print(antall_dager_mellom_datoer("01/01/2024", "21/11/2024"))  # Output: 325
print(antall_dager_mellom_datoer("15/08/2023", "15/08/2023"))  # Output: 0
print(antall_dager_mellom_datoer("31/12/2023", "01/01/2024"))  # Output: 1
