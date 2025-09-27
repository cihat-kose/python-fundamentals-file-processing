"""
Oppgave 3.4
Lag en funksjon som tar en annen funksjon som parameter, noen argumenter og et forventet resultat,
og som returnerer sant hvis det faktiske resultatet stemmer overens med det forventede resultatet, ellers usant.
"""


def sjekk_funksjon(funksjon, argumenter, forventet_resultat):
    faktisk_resultat = funksjon(*argumenter)
    return faktisk_resultat == forventet_resultat


def addisjon(a, b):
    return a + b


def subtraksjon(a, b):
    return a - b


def multiplikasjon(a, b):
    return a * b


# Test tilfeller
print(sjekk_funksjon(addisjon, [3, 4], 7))  # Output: True
print(sjekk_funksjon(addisjon, [3, 4], 8))  # Output: False
print(sjekk_funksjon(subtraksjon, [10, 4], 6))  # Output: True
print(sjekk_funksjon(multiplikasjon, [3, 4], 12))  # Output: True
