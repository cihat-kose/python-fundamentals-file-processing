"""Build a name-to-age dictionary from alternating names and ages."""


def main():
    names_and_ages = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

    ages_by_name = {names_and_ages[i]: names_and_ages[i + 1] for i in range(0, len(names_and_ages), 2)}

    for name, age in ages_by_name.items():
        print(f"{name} is {age} years old")


if __name__ == "__main__":
    main()
