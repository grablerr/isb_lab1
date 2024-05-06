from cryptosystem import generate_keys, encrypt_text, decrypt_text


def main():
    key_length = 16
    enc_symmetric, private_key, public_key = generate_keys(key_length)

    print(enc_symmetric)

    original_text = "Пример текста для шифрования и дешифрования."

    encrypted_text = encrypt_text(original_text, enc_symmetric, private_key)
    print("Зашифрованный текст:", encrypted_text)

    decrypted_text = decrypt_text(encrypted_text, enc_symmetric, private_key)
    print("Расшифрованный текст:", decrypted_text)


if __name__ == "__main__":
    main()
