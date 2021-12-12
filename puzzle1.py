import pandas as pd


def part_one(values, nb_values):
    print("--- Running part_one ---")

    # Solve puzzle
    prev = values[0]
    nb_increases = 0
    for i in range(1, nb_values):
        if values[i] > prev:
            nb_increases += 1
        prev = values[i]

    # Print result
    print("part_one nb_increases =", nb_increases)


def part_two(values, nb_values):
    print("--- Running part_two ---")

    # Solve puzzle
    prev = values[0] + values[1] + values[2]
    nb_increases = 0
    for i in range(1, nb_values-2):
        current = values[i] + values[i+1] + values[i+2]
        if current > prev:
            nb_increases += 1
        prev = current

    # Print result
    print("part_two nb_increases =", nb_increases)


# Load data
input = pd.read_csv("data/data_puzzle1.csv", header=None)
input_values = input.iloc[:, 0].tolist()
nb_values = len(input_values)

# Run algos
part_one(input_values, nb_values)
part_two(input_values, nb_values)
