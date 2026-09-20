"""Compare the character counts of two sentences."""


def main():
    sentence1 = input("Enter the first sentence: ")
    sentence2 = input("Enter the second sentence: ")

    length1 = len(sentence1)
    length2 = len(sentence2)

    if length1 > length2:
        print(f"The longest sentence is \"{sentence1}\" with character count {length1}")
    elif length2 > length1:
        print(f"The longest sentence is \"{sentence2}\" with character count {length2}")
    else:
        print(f"Both sentences have the same character count: {length1}")


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Please enter valid integers.")
