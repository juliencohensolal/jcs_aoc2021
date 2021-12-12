import pandas as pd


def part_one(input, nb_bits):
    print("--- Running part_one ---")

    # Solve puzzle
    gamma, epsilon = "", ""
    for i in range(nb_bits):
        frequencies = input.iloc[:, i].value_counts()
        gamma += str(frequencies.index[0])
        epsilon += str(frequencies.index[-1])
    decimal_gamma = int(gamma, 2)
    decimal_espilon = int(epsilon, 2)
    consumption = decimal_gamma * decimal_espilon

    # Print result
    print("part_one decimal_gamma, decimal_espilon =", decimal_gamma, decimal_espilon)
    print("part_one consumption =", consumption)


def part_two(input, nb_bits):
    print("--- Running part_two ---")

    # Solve puzzle
    oxygen_df = input.copy()
    scrubber_df = input.copy()
    for i in range(nb_bits):
        frequencies_ox = oxygen_df.iloc[:, i].value_counts()
        frequencies_sc = scrubber_df.iloc[:, i].value_counts()
        
        if oxygen_df.shape[0] > 1:
            if frequencies_ox[0] == frequencies_ox[1]:
                # Edge case, keep "1"
                most_common = "1"
            else:
                most_common = frequencies_ox.index[0]
            oxygen_df = oxygen_df.loc[oxygen_df[i] == most_common]
        if scrubber_df.shape[0] > 1:
            if frequencies_sc[0] == frequencies_sc[1]:
                # Edge case, keep "0"
                least_common = "0"
            else:
                least_common = frequencies_sc.index[-1]
            scrubber_df = scrubber_df.loc[scrubber_df[i] == least_common]
    
    oxygen, scrubber = "", ""
    for i in range(nb_bits):
        oxygen += str(oxygen_df.iloc[0, i])
        scrubber += str(scrubber_df.iloc[0, i])
    oxygen = int(oxygen, 2)
    scrubber = int(scrubber, 2)
    life_support = oxygen * scrubber

    # Print result
    print("part_two oxygen, scrubber =", oxygen, scrubber)
    print("part_two life_support =", life_support)


# Load data
input = pd.read_csv("data/data_puzzle3.csv", header=None, dtype=str)
input = input.iloc[:, 0].astype(str).apply(lambda x: pd.Series(list(x)))
nb_values = input.shape[0]
nb_bits = input.shape[1]

# Run algos
part_one(input, nb_bits)
part_two(input, nb_bits)
