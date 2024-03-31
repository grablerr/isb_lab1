from square import punctuation_symbols


def encrypt_with_polybius_square(message: str, square: dict) -> str:
    encrypted_text = ""
    try:
        for char in message:
            if char.lower() in punctuation_symbols:
                encrypted_text += char
            else:
                try:
                    encrypted_char = square.get(char)
                    encrypted_text += encrypted_char
                except Exception as exc:
                    print(f"An exception occurred while encrypting character '{char}': {exc}")
    except Exception as exc:
        print(f"An exception was found. Exception name - {exc}")
    return encrypted_text


def main() -> None:



if __name__ == "__main__":
    main()
