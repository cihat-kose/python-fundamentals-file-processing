"""Print the multiplication table for an integer, from 1 to 10."""


def main():
    number = int(input("Enter an integer: "))

    for multiplier in range(1, 11):
        print(f"{number} * {multiplier} = {number * multiplier}")


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Please enter valid integers.")
