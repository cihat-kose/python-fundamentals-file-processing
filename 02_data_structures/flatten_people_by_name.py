"""Flatten a name-to-age dictionary in alphabetical name order."""


def main():
    names_and_ages = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

    ages_by_name = {}
    for i in range(0, len(names_and_ages), 2):
        ages_by_name[names_and_ages[i]] = names_and_ages[i + 1]

    sorted_names = sorted(ages_by_name.keys())

    sorted_list = []
    for name in sorted_names:
        sorted_list.append(name)
        sorted_list.append(ages_by_name[name])

    print(sorted_list)


if __name__ == "__main__":
    main()
