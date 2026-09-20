"""Validate calendar dates entered in day/month/year order."""


def is_valid_date(value):
    """Return whether value describes a valid date, including leap years."""
    try:
        day_text, month_text, year_text = value.split("/")
        day = int(day_text)
        month = int(month_text)
        year = int(year_text)
    except (AttributeError, ValueError):
        return False

    if year <= 0 or not 1 <= month <= 12:
        return False

    leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    days_in_month = [31, 29 if leap_year else 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    return 1 <= day <= days_in_month[month - 1]


if __name__ == "__main__":
    value = input("Enter a date (dd/mm/yyyy): ")
    print("Valid date" if is_valid_date(value) else "Invalid date")
