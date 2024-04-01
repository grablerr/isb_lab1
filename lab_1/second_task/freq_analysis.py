from work_with_json_file import read_path_file
from alphabet import path, alph_pas
from collections import defaultdict


def get_text(file_path: str) -> str:
    """
       Read text content from a file.

       Args:
           file_path (str): The path to the file to be read.

       Returns:
           str: The text content read from the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return " "
    except Exception as e:
        print(f"An error occurred: {e}")
        return " "


def calculate_freq(text: str):
    """
        Calculate the frequency of characters in the given text.

        Parameters:
            text (str): The text for which character frequencies are calculated.

        Returns:
            None
        """
    try:
        quantity = defaultdict(int)
        for char in text:
            quantity[char] += 1
        total_quantity = sum(quantity.values())
        sorted_frequencies = sorted(
            quantity.items(), key=lambda x: x[1], reverse=True
        )
        frequencies = {}
        for char, freq in sorted_frequencies:
            decimal_freq = freq / total_quantity
            frequencies[char] = decimal_freq

        with open(alph_pas, "a", encoding="utf-8") as file:
            file.write("frequencies = " + str(frequencies) + "\n")

    except Exception as e:
        print(f"An error occurred: {e}")
        return


def main():
    json_data = read_path_file(path)
    folder_path = json_data[0]
    input_file = json_data[1]
    input_file_path = f"{folder_path}/{input_file}"
    text = get_text(input_file_path)
    calculate_freq(text)


if __name__ == "__main__":
    main()
