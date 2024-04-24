from math import sqrt
from scipy.special import erfc
from constants_and_paths import CPP, JAVA


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


def main():
    cpp_sequence = get_sequence(CPP)
    java_sequence = get_sequence(JAVA)
    print(same_consecutive_bits_test(cpp_sequence))
    print(same_consecutive_bits_test(java_sequence))


if __name__ == "__main__":
    main()
