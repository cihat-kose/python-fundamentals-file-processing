"""Average loan period. See README.md for source fields."""

import csv
from pathlib import Path


def average_loan_period(filename):
    """Return the average duration truncated to the required whole day."""
    total_days = 0
    count = 0

    with open(filename, "r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row_number, row in enumerate(reader, start=2):
            loan_period_text = (row.get("Låneperiode") or "").strip()
            extension_text = (row.get("Forlenget") or "").strip()

            if loan_period_text == "" or extension_text == "":
                continue

            try:
                loan_period_days = int(loan_period_text)
                extension_days = int(extension_text)
                if loan_period_days < 0 or extension_days < 0:
                    raise ValueError("negative value")
                total_days += loan_period_days + extension_days
                count += 1
            except ValueError:
                print(
                    f"Invalid value in row {row_number}: "
                    f"loan_period={loan_period_text!r}, "
                    f"extension={extension_text!r}"
                )

    if count == 0:
        print("No valid rows to average.")
        return None

    average = total_days // count
    print(f"Average loan period (including extensions): {average} days")
    return average


if __name__ == "__main__":
    average_loan_period(Path(__file__).with_name("library_loans.csv"))
