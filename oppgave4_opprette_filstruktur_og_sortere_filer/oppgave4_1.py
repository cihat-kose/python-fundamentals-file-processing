"""
Oppgave 4.1
Lag en funksjon som oppretter en mappe kalt Files og genererer 30 tilfeldige filer
med følgende filtyper i denne mappen: .txt, .csv, og .log.

Hver fil skal ha:
- Et tilfeldig navn med mellom 5 og 10 tegn.
- En tilfeldig filtype valgt fra de tre typene.
- Innhold i disse filene er ikke viktig — lag gjerne disse filene uten innhold.

Eksempel (struktur):

Files
|-- G5zLehz4.txt
|-- iTwTrTkU.txt
|-- vPcaO7jR.csv
|-- 1Vgi2jbe.log
‘-- 7NMaq7aa.csv

0 directories, 5 files
"""

import os
import random
import shutil
import string


def generer_tilfeldig_streng(lengde):
    bokstaver = string.ascii_letters + string.digits
    return ''.join(random.choice(bokstaver) for _ in range(lengde))


def opprett_tilfeldige_filer(mappe, antall_filer):
    filtyper = ['.txt', '.csv', '.log']

    if os.path.exists(mappe):
        shutil.rmtree(mappe)
    os.makedirs(mappe)

    for _ in range(antall_filer):
        filnavn_lengde = random.randint(5, 10)
        filnavn = generer_tilfeldig_streng(filnavn_lengde)
        filtype = random.choice(filtyper)
        filsti = os.path.join(mappe, filnavn + filtype)

        with open(filsti, 'w'):
            pass


def skriv_mappestruktur(mappe):
    filer = os.listdir(mappe)
    print(mappe)
    for fil in filer:
        print(f"|-- {fil}")
    print(f"0 mapper, {len(filer)} filer")


if __name__ == "__main__":
    mappe_navn = "Files"
    antall_filer = 30
    opprett_tilfeldige_filer(mappe_navn, antall_filer)
    skriv_mappestruktur(mappe_navn)
