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


def main():
    cpp_sequence = get_sequence(CPP)
    java_sequence = get_sequence(JAVA)
    print(freq_bit_test(cpp_sequence))
    print(freq_bit_test(java_sequence))


if __name__ == "__main__":
    main()
