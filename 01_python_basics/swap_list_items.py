"""Swap two items using non-negative list indices."""


def main():
    fruits = ["apple", "banana", "orange", "grape", "kiwi"]

    try:
        first_index = int(input("Enter the first index: "))
        second_index = int(input("Enter the second index: "))

        if 0 <= first_index < len(fruits) and 0 <= second_index < len(fruits):
            fruits[first_index], fruits[second_index] = fruits[second_index], fruits[first_index]
            print(f"Updated list: {fruits}")
        else:
            print(f"Invalid index. Enter values from 0 to {len(fruits) - 1}.")

    except ValueError:
        print("Invalid input. Please enter whole-number indices.")


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Invalid input. Please enter whole-number indices.")
