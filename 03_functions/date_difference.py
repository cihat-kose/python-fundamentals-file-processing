"""Calculate the absolute number of days between two dates."""

from datetime import datetime


def days_between_dates(first_date, second_date):
    """Parse day/month/year strings; raise ValueError for invalid dates."""
    first = datetime.strptime(first_date, "%d/%m/%Y")
    second = datetime.strptime(second_date, "%d/%m/%Y")
    return abs((second - first).days)


if __name__ == "__main__":
    print(days_between_dates("21/11/2024", "01/01/2024"))
