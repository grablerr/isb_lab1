from cryptosystem import generate_keys


def main():
    key_length = 16
    enc_symmetric, private_key, public_key = generate_keys(key_length)

    print(enc_symmetric)
    print(private_key)
    print(public_key)


if __name__ == "__main__":
    main()
