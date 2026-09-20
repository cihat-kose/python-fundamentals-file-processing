"""Sort people by age, oldest first."""


def main():
    names_and_ages = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

    ages_by_name = {}

    for pair_index in range(0, len(names_and_ages), 2):
        ages_by_name[names_and_ages[pair_index]] = names_and_ages[pair_index + 1]

    sorted_names = sorted(ages_by_name, key=ages_by_name.get, reverse=True)

    for name in sorted_names:
        print(f"{name} is {ages_by_name[name]} years old")


if __name__ == "__main__":
    main()
