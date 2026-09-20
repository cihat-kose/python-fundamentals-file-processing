"""Count loans by genre. See dataset_overview.py for source fields."""

import csv
from pathlib import Path
from collections import Counter


def count_loans_by_genre(filename):
    valid_genres = {"Fiksjon", "Krim", "Sakprosa", "Fantasy"}
    counts = Counter()

    with open(filename, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            genre = (row.get("Sjanger") or "").strip()
            if genre in valid_genres:
                counts[genre] += 1
            elif genre:
                print(f"Unrecognized genre: {genre}")

    return counts


if __name__ == "__main__":
    result = count_loans_by_genre(Path(__file__).with_name("library_loans.csv"))
    for genre, count in result.items():
        labels = {"Fiksjon": "Fiction", "Krim": "Crime", "Sakprosa": "Nonfiction", "Fantasy": "Fantasy"}
        print(f"{labels[genre]}: {count}")
