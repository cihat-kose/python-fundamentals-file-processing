"""Convert alternating names and ages into person dictionaries."""


def main():
    names_and_ages = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

    dictionary_list = []

    for pair_index in range(0, len(names_and_ages), 2):
        name = names_and_ages[pair_index]
        age = names_and_ages[pair_index + 1]
        dictionary_list.append({"name": name, "age": age})

    print(dictionary_list)


if __name__ == "__main__":
    main()
