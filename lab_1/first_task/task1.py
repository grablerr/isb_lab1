from work_with_json_file import read_path_file
from square import polybius_square, punctuation_symbols, path


def encrypt_with_polybius_square(message: str, square: list) -> str:
    """
    Encrypts a message using a Polybius square.
    Args:
        message (str): The message to be encrypted.
        square (list): The Polybius square as a list of lists where each sublist represents a row
                       and contains encrypted symbols corresponding to uppercase letters.
    Returns:
        str: The encrypted message.
    """
    encrypted_text = ""
    message = message.upper()
    try:
        for char in message:
            if char in punctuation_symbols:
                encrypted_text += char
            else:
                char_found = False
                for i, row in enumerate(square):
                    if char in row:
                        col = row.index(char)
                        encrypted_text += f"({i + 1}{col + 1})"
                        char_found = True
                        break
                if not char_found:
                    raise ValueError(
                        f"Character '{char}' not found in the Polybius square."
                    )
    except Exception as e:
        print("An error occurred:", e)
        return
    return encrypted_text


def main() -> None:
    """
    Encrypts the text from an input file using a Polybius square and saves the encrypted text to an output file.

    Reads paths data from a JSON file, where 'folder', 'input_text', and 'output_text' keys specify the folder path,
    input file name, and output file name respectively.

    If paths data is successfully read and all necessary paths are provided, the function reads the input file,
    encrypts its content using a Polybius square, and saves the encrypted text to the output file.

    Prints success message if encryption and file saving are successful.
    Prints error messages for file not found and other exceptions.
    """
    paths_data = read_path_file(path)
    if paths_data:
        folder = paths_data[0]
        input_text = paths_data[1]
        output_text = paths_data[2]

        if folder and input_text and output_text:
            try:
                with open(f"{folder}/{input_text}", "r", encoding="utf-8") as file:
                    text = file.read()
                    encrypted_text = encrypt_with_polybius_square(text, polybius_square)

                with open(f"{folder}/{output_text}", "w", encoding="utf-8") as file:
                    file.write(encrypted_text)

                print(f"Message encryption success and saved into {output_text}.")
            except FileNotFoundError:
                print("File not found.")
            except Exception as e:
                print(f"Fail - : {e}")
        else:
            print("Couldn't get file paths from JSON data.")
    else:
        print("Data could not be read from the JSON file.")


if __name__ == "__main__":
    main()
