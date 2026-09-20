"""Sum loan extensions. See README.md for source fields."""

import csv
from pathlib import Path


def sum_loan_extensions(filename):
    total = 0
    with open(filename, "r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            value = (row.get("Forlenget") or "").strip()
            if not value:
                continue
            try:
                days = int(value)
                if days < 0:
                    raise ValueError("negative value")
            except ValueError:
                print(f"Invalid extension value: {value!r}")
                continue
            total += days
    return total


if __name__ == "__main__":
    result = sum_loan_extensions(Path(__file__).with_name("library_loans.csv"))
    print(f"Total extension days: {result}")
