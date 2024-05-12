from symmetric_method import generate_symmetric_key, encrypt_text, decrypt_text


def main():
    key_length = 16
    symmetric_key = generate_symmetric_key(key_length)

    print(generate_symmetric_key(key_length))

    original_text = "Пример текста для шифрования и дешифрования."

    encrypted_text = encrypt_text(original_text, symmetric_key)
    print("Зашифрованный текст:", encrypted_text)

    decrypted_text = decrypt_text(encrypted_text, symmetric_key)
    print("Расшифрованный текст:", decrypted_text)


if __name__ == "__main__":
    main()
