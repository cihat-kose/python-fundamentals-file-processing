"""Average loan period. See dataset_overview.py for source fields."""

import csv
from pathlib import Path


def average_loan_period(filename):
    total_days = 0
    count = 0

    with open(filename, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            lp = (row.get("Låneperiode") or "").strip()
            ext = (row.get("Forlenget") or "").strip()

            if lp == "" or ext == "":
                continue

            try:
                lp_i = int(lp)
                ext_i = int(ext)
                if lp_i < 0 or ext_i < 0:
                    raise ValueError("negative value")
                total_days += lp_i + ext_i
                count += 1
            except ValueError:
                print(f"Invalid value in row {i}: Låneperiode={lp!r}, Forlenget={ext!r}")

    if count == 0:
        print("No valid rows to average.")
        return None

    average = total_days // count
    print(f"Average loan period (including extensions): {average} days")
    return average


if __name__ == "__main__":
    average_loan_period(Path(__file__).with_name("library_loans.csv"))
