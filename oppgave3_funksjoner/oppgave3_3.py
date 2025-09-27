"""
Oppgave 3.3
I dataprogrammering brukes fargekoder ofte for å representere farger i brukergrensesnitt og grafikk.
To vanlige måter å representere farger på er:

1. Hex-kode: En fargekode som starter med # og består av seks tegn som representerer de røde, grønne og blå komponentene
   i fargen (for eksempel #CD5C5C). Hver komponent har to tegn (heksadesimalt), hvor:
   - CD representerer rødt (r),
   - 5C representerer grønt (g),
   - 5C representerer blått (b).

2. RGB-kode: En fargekode representert som tre heltall, én for hver fargekomponent (rød, grønn, blå).
   For eksempel: rgb(205, 92, 92).

Lag en funksjon rgb_to_hex som tar inn tre heltall (for eksempel red=205, green=92, blue=92)
og returnerer tilsvarende Hex-kode som en streng (for eksempel "#CD5C5C").
Legg også til passende feilmelding om red, blue eller green parametere har ugyldig verdi.
"""


def rgb_til_hex(rød, grønn, blå):
    if not (0 <= rød <= 255):
        return "Feil: Rød verdi må være mellom 0 og 255"
    if not (0 <= grønn <= 255):
        return "Feil: Grønn verdi må være mellom 0 og 255"
    if not (0 <= blå <= 255):
        return "Feil: Blå verdi må være mellom 0 og 255"

    hex_rød = f"{rød:02X}"
    hex_grønn = f"{grønn:02X}"
    hex_blå = f"{blå:02X}"

    hex_kode = f"#{hex_rød}{hex_grønn}{hex_blå}"

    return hex_kode


# Test tilfeller
print("Test 1: rgb_til_hex(205, 92, 92)")
print("Output:", rgb_til_hex(205, 92, 92))  # Output: #CD5C5C

print("Test 2: rgb_til_hex(0, 0, 0)")
print("Output:", rgb_til_hex(0, 0, 0))  # Output: #000000

print("Test 3: rgb_til_hex(255, 255, 255)")
print("Output:", rgb_til_hex(255, 255, 255))  # Output: #FFFFFF

print("Test 4: rgb_til_hex(256, 0, 0)")
print("Output:", rgb_til_hex(256, 0, 0))  # Output: Feil: Rød verdi må være mellom 0 og 255

print("Test 5: rgb_til_hex(0, 256, 0)")
print("Output:", rgb_til_hex(0, 256, 0))  # Output: Feil: Grønn verdi må være mellom 0 og 255

print("Test 6: rgb_til_hex(0, 0, 256)")
print("Output:", rgb_til_hex(0, 0, 256))  # Output: Feil: Blå verdi må være mellom 0 og 255
