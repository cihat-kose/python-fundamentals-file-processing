"""Split alternating names and ages into separate lists."""


def main():
    names_and_ages = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

    names = [names_and_ages[i] for i in range(0, len(names_and_ages), 2)]
    ages = [names_and_ages[i] for i in range(1, len(names_and_ages), 2)]

    print("Names:", names)
    print("Ages:", ages)


if __name__ == "__main__":
    main()
