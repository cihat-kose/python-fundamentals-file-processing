"""Sum the integers from 1 to a positive integer using a loop."""


def main():
    number = int(input("Enter a positive integer: "))

    if number <= 0:
        print("Please enter a positive integer.")
        return

    total = 0

    for i in range(1, number + 1):
        total += i

    print(f"The sum of integers from 1 to {number} (inclusive) is: {total}")


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Please enter valid integers.")
