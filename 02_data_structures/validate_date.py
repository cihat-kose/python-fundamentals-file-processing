"""Validate calendar dates entered in day/month/year order."""

from datetime import datetime


def is_valid_date(value):
    """Return whether value describes a valid date (years 1 through 9999)."""
    try:
        datetime.strptime(value, "%d/%m/%Y")
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    value = input("Enter a date (dd/mm/yyyy): ")
    print("Valid date" if is_valid_date(value) else "Invalid date")
