"""Count loans by genre. See README.md for source fields."""

import csv
from pathlib import Path
from collections import Counter


def count_loans_by_genre(filename):
    valid_genres = {"Fiction", "Crime", "Nonfiction", "Fantasy"}
    counts = Counter()

    with open(filename, "r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            genre = (row.get("genre") or "").strip()
            if genre in valid_genres:
                counts[genre] += 1
            elif genre:
                print(f"Unrecognized genre: {genre}")

    return counts


if __name__ == "__main__":
    result = count_loans_by_genre(Path(__file__).with_name("library_loans.csv"))
    for genre, count in result.items():
        print(f"{genre}: {count}")
