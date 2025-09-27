"""
Fil Analyse – Introduksjon

Du har fått tilgang til en fil som heter bokutlån.csv. Filen inneholder informasjon om bøker som har blitt lånt ut fra et bibliotek over en gitt periode. Informasjonen er registrert i følgende kolonner:
1. Fornavn – Fornavnet til personen som lånte boken.
2. Etternavn – Etternavnet til personen som lånte boken.
3. Boktittel – Navnet på boken som ble lånt.
4. Sjanger – Sjanger på boken som ble lånt (Fiksjon, Krim, Sakprosa, Fantasy).
5. Lånedato – Datoen boken ble lånt ut (dd/mm/yyyy).
6. Låneperiode – Antall dager boken er lånt (standard: 14 dager).
7. Forlenget – Hvor mange ekstra dager lånet ble forlenget (kan være 0).
8. Tilbakelevert – Om boken ble levert tilbake i tide (Ja/Nei).

Programmet må kunne håndtere:
• Manglende data: Rader med manglende felt ignoreres, men beregninger fullføres.
• Ugyldige verdier: Hvis numeriske kolonner (f.eks. forlengelse eller låneperiode) ikke er tall, skal programmet håndtere dette og gi en forklaring.

Tips: Åpne filen med UTF-8: open(filename, 'r', encoding='utf-8')
"""
