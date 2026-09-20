"""Print the multiplication table for an integer, from 1 to 10."""


def main():
    number = int(input("Enter an integer: "))

    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Please enter valid integers.")
