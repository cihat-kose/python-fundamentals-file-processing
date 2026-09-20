"""Most borrowed books. See README.md for source fields."""

import csv
from pathlib import Path
from collections import Counter


def most_borrowed_books(filename):
    counts = Counter()
    with open(filename, "r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            book = (row.get("book_title") or "").strip()
            if book:
                counts[book] += 1

    if not counts:
        return []

    maximum = max(counts.values())

    most = [(title, count) for title, count in counts.items() if count == maximum]

    def alphabetical(element):
        return element[0]

    most.sort(key=alphabetical)

    return most


if __name__ == "__main__":
    results = most_borrowed_books(Path(__file__).with_name("library_loans.csv"))
    print("Most borrowed books:")
    for title, count in results:
        print(f"- {title} ({count} loans)")
