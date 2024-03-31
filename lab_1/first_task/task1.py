from square import punctuation_symbols


def encrypt_with_polybius_square(message: str, square: dict) -> str:
    encrypted_text = ""
    try:
        for char in message:
            if char.upper() in punctuation_symbols:
                encrypted_text += char
            else:
                char_lower = char.upper()
                try:
                    encrypted_char = square.get(char_lower)
                    if encrypted_char:
                        encrypted_text += "(" + encrypted_char + ")"
                    else:
                        encrypted_text += char  # Возвращаем исходный символ, если нет соответствия в словаре
                except Exception as e:
                    print(f"An exception occurred while encrypting character '{char}': {e}")
    except Exception as exception:
        print(f"An exception was found. Exception name - {exception}")
    return encrypted_text


def main() -> None:
    polybius_square = {"А": "11", "Б": "12", "В": "13", "Г": "14", "Д": "15", "Е": "16",
                       "Ё": "21", "Ж": "22", "З": "23", "И": "24", "Й": "25", "К": "26",
                       "Л": "31", "М": "32", "Н": "33", "О": "34", "П": "35", "Р": "36",
                       "С": "41", "Т": "42", "У": "43", "Ф": "44", "Х": "45", "Ц": "46",
                       "Ч": "51", "Ш": "52", "Щ": "53", "Ъ": "54", "Ы": "55", "Ь": "56",
                       "Э": "61", "Ю": "62", "Я": "63", " ": "64"}

    encrypted_message = encrypt_with_polybius_square("Привет мир!", polybius_square)
    print(encrypted_message)


if __name__ == "__main__":
    main()
