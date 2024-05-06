from math import sqrt
from scipy.special import erfc
from mpmath import gammainc

from constants_and_paths import CPP, JAVA, PI_VALUES, BLOCK_SIZE


def get_sequence(file_name):
    """
    Read and return the content(binary sequence) of a file .

    Args:
        file_name (str): Name of the file to read.

    Returns:
        str: Content of the file.
    """
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{file_name}' not found")
        return None
    except Exception as e:
        print(f"An error while reading file: {e}")
        return None


def freq_bit_test(sequence: str) -> float:
    """
    Calculate the frequency test for a binary sequence.

    Args:
        sequence (str): A binary sequence to be tested.

    Returns:
        float: The p-value calculated for the test.
    """
    try:
        p_value = erfc((sum(1 if bit == "1" else -1 for bit in sequence) / sqrt(len(sequence))) / sqrt(2))
        return p_value
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1


def same_consecutive_bits_test(sequence: str) -> float:
    """
    Calculation of the test for the same consecutive bits.

    Args:
        sequence (str): A binary sequence to be tested.

    Returns:
        float: The p-value calculated for the test.
    """
    try:
        proportion_of_ones = sequence.count("1") / len(sequence)
        if abs(proportion_of_ones - 0.5) >= 2 / sqrt(len(sequence)):
            return 0
        vn = sum(1 if sequence[i] != sequence[i + 1] else 0 for i in range(len(sequence) - 1))
        p_value = erfc(
            (abs(vn - 2 * len(sequence) * proportion_of_ones * (1 - proportion_of_ones)))
            / (2 * sqrt(2 * len(sequence)) * proportion_of_ones * (1 - proportion_of_ones))
        )
        return p_value
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def long_sequence_units_test(sequence: str) -> float:
    """
    Calculate the long sequence units test for a binary sequence.

    Args:
        sequence (str): A binary sequence to be tested.

    Returns:
        float: The p-value calculated for the test.
    """
    try:
        blocks = [
            sequence[i: i + BLOCK_SIZE] for i in range(0, len(sequence), BLOCK_SIZE)
        ]
        statistics = {"v1": 0, "v2": 0, "v3": 0, "v4": 0}
        for block in blocks:
            max_ones = 0
            current_ones = 0
            for bit in block:
                if bit == "1":
                    current_ones += 1
                    max_ones = max(max_ones, current_ones)
                else:
                    current_ones = 0
            match max_ones:
                case 0 | 1:
                    statistics["v1"] += 1
                case 2:
                    statistics["v2"] += 1
                case 3:
                    statistics["v3"] += 1
                case _:
                    statistics["v4"] += 1
        chi_square = sum(
            ((statistics[f"v{i + 1}"] - 16 * PI_VALUES[i]) ** 2) / (16 * PI_VALUES[i])
            for i in range(4)
        )
        p_value = gammainc(1.5, chi_square / 2)
        return p_value
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    cpp_sequence = get_sequence(CPP)
    java_sequence = get_sequence(JAVA)
    print(f"Results of the frequency bitwise test:\nCPP: " + str(freq_bit_test(cpp_sequence)) + "\nJAVA: " + str(
        freq_bit_test(java_sequence)) + "\n")
    print(f"Test results for the same consecutive bits:\nCPP: " + str(
        same_consecutive_bits_test(cpp_sequence)) + "\nJAVA: " + str(same_consecutive_bits_test(java_sequence)) + "\n")
    print(f"Test results for the longest sequence of units in a block:\nCPP: " + str(
        long_sequence_units_test(cpp_sequence)) + "\nJAVA: " + str(long_sequence_units_test(java_sequence)) + "\n")


if __name__ == "__main__":
    main()
