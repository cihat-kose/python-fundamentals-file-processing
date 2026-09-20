"""List unreturned books. See README.md for source fields."""

import csv
from pathlib import Path


def list_unreturned_books(filename):
    result = []

    with open(filename, "r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            returned = (row.get("Tilbakelevert") or "").strip().lower()
            if returned == "nei":
                first_name = (row.get("Fornavn") or "").strip()
                last_name = (row.get("Etternavn") or "").strip()
                book = (row.get("Boktittel") or "").strip()
                if book and first_name and last_name:
                    result.append((book, f"{first_name} {last_name}"))

    return result


if __name__ == "__main__":
    books = list_unreturned_books(Path(__file__).with_name("library_loans.csv"))
    if not books:
        print("No records explicitly marked as unreturned.")
    else:
        print("Unreturned books:")
        for book, name in books:
            print(f"- {book} (borrowed by {name})")
