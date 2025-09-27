"""
Oppgave 4.2
Lag en funksjon som leser filene i Files og sorterer dem i undermapper basert på filtype:

- Opprett en ny mappe kalt SortedFiles.
- Opprett undermapper kalt txt, csv, og log inne i denne mappen kalt SortedFiles.
- Flytt filene fra Files til riktig undermappe i SortedFiles basert på deres filtype.

Eksempel (struktur):

SortedFiles
|-- csv
|   |-- vPcaO7jR.csv
|   ‘-- 7NMaq7aa.csv
|-- log
|   ‘-- 1Vgi2jbe.log
‘-- txt
    |-- G5zLehz4.txt
    ‘-- iTwTrTkU.txt

3 directories, 5 files
"""

import os
import shutil


def sorter_filer():
    kilde_mappe = "Files"
    dest_mappe = "SortedFiles"

    if os.path.exists(dest_mappe):
        shutil.rmtree(dest_mappe)

    os.makedirs(os.path.join(dest_mappe, "txt"))
    os.makedirs(os.path.join(dest_mappe, "csv"))
    os.makedirs(os.path.join(dest_mappe, "log"))

    for fil in os.listdir(kilde_mappe):
        filsti = os.path.join(kilde_mappe, fil)

        if fil.endswith(".txt"):
            shutil.move(filsti, os.path.join(dest_mappe, "txt", fil))
        elif fil.endswith(".csv"):
            shutil.move(filsti, os.path.join(dest_mappe, "csv", fil))
        elif fil.endswith(".log"):
            shutil.move(filsti, os.path.join(dest_mappe, "log", fil))
    print("Filer er sortert og flyttet til 'SortedFiles'.")


if __name__ == "__main__":
    sorter_filer()
