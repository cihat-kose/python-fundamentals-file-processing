"""List unreturned books. See README.md for source fields."""

import csv
from pathlib import Path


def list_unreturned_books(filename):
    result = []

    with open(filename, "r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            returned = (row.get("returned") or "").strip().lower()
            if returned == "no":
                borrower_id = (row.get("borrower_id") or "").strip()
                book = (row.get("book_title") or "").strip()
                if book and borrower_id:
                    result.append((book, borrower_id))

    return result


if __name__ == "__main__":
    books = list_unreturned_books(Path(__file__).with_name("library_loans.csv"))
    if not books:
        print("No complete records explicitly marked as unreturned.")
    else:
        print("Unreturned books:")
        for book, name in books:
            print(f"- {book} (borrowed by {name})")
