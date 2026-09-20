"""Sort people by age, oldest first."""


def main():
    names_and_ages = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

    ages_by_name = {}

    for i in range(0, len(names_and_ages), 2):
        ages_by_name[names_and_ages[i]] = names_and_ages[i + 1]

    sorted_names = sorted(ages_by_name, key=ages_by_name.get, reverse=True)

    for i in sorted_names:
        print(f"{i} is {ages_by_name[i]} years old")


if __name__ == "__main__":
    main()
