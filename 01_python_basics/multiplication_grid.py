"""Print a multiplication grid for an inclusive integer interval."""


def main():
    start = int(input("Enter the start (m): "))
    end = int(input("Enter the end (n): "))

    if start > end:
        print("The start must not exceed the end.")
        return

    cell_width = max(3, len(str(start)), len(str(end)),
                     len(str(start * start)), len(str(end * end)),
                     len(str(start * end)))

    header = "| " + " | ".join(
        f"{column:>{cell_width}}" for column in range(start, end + 1)
    ) + " |"
    separator = "| " + " | ".join(
        "-" * cell_width for _ in range(start, end + 1)
    ) + " |"
    print(header)
    print(separator)

    for row_value in range(start, end + 1):
        row = "| " + " | ".join(
            f"{row_value * column_value:>{cell_width}}"
            for column_value in range(start, end + 1)
        ) + " |"
        print(row)


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Please enter valid integers.")
