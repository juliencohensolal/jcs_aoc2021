import pandas as pd


def part_one(input, nb_values):
    print("--- Running part_one ---")

    # Solve puzzle
    x, y = 0, 0
    directions = input["direction"].tolist()
    lengths = input["length"].tolist()
    for i in range(nb_values):
        if directions[i] == "forward":
            x += int(lengths[i])
        elif directions[i] == "down":
            y += int(lengths[i])
        else: # up
            y -= int(lengths[i])

    # Print result
    print("part_one x, y =", x, y)
    print("part_one result =", x*y)


def part_two(input, nb_values):
    print("--- Running part_two ---")

    # Solve puzzle
    x, y, aim = 0, 0, 0
    directions = input["direction"].tolist()
    lengths = input["length"].tolist()
    for i in range(nb_values):
        if directions[i] == "forward":
            x += int(lengths[i])
            y += aim * int(lengths[i])
        elif directions[i] == "down":
            aim += int(lengths[i])
        else: # up
            aim -= int(lengths[i])

    # Print result
    print("part_two x, y =", x, y)
    print("part_two result =", x*y)


# Load data
input = pd.read_csv("data/data_puzzle2.csv", header=None)
input = input.iloc[:, 0].str.split(" ", expand=True)
input.columns = ["direction", "length"]
nb_values = input.shape[0]

# Run algos
part_one(input, nb_values)
part_two(input, nb_values)
