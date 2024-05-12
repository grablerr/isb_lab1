import argparse

from enum import Enum

from asymmetric_method import *
from symmetric_method import *
from file_for_work_with_data import *
from file_for_serialization import *


class Option(Enum):
    GENERATE_SYMMETRIC_KEY = 0
    GENERATE_ASYMMETRIC_KEYS = 1
    ENCRYPT_TEXT = 2
    DECRYPT_TEXT = 3
    ENCRYPT_SYMMETRIC_KEY = 4
    DECRYPT_SYMMETRIC_KEY = 5


if __name__ == "__main__":
    parser = argparse.ArgumentParser("")
    parser.add_argument("option", type=int,
                        help="Выбор режима работы: "
                             "0-генерация симметричного ключа"
                             "1-генерация ассимметричных ключей"
                             "2-шифрование текста"
                             "3-дешифрование текста"
                             "4-шифрование симметричного ключа"
                             "5-дешифрование симметричного ключа")
    parser.add_argument("settings", type=str,
                        help="Введите путь к файлу с пользовательскими настройками")
    args = parser.parse_args()

    settings = read_json("settings.json")
    match (args.option):
        case Option.GENERATE_SYMMETRIC_KEY.value:
            symmetric_key = generate_symmetric_key(16)
            save_symmetric_key(settings["symmetric_key"], symmetric_key)
        case Option.GENERATE_ASYMMETRIC_KEYS.value:
            private_key, public_key = generate_asymmetric_keys()
            save_public_key(settings["public_key"], public_key)
            save_private_key(settings["private_key"], private_key)

        case Option.ENCRYPT_TEXT.value:
            encrypted_text = encrypt_text(read_text(settings["source_text"]), read_bytes(settings["symmetric_key"]))
            save_bytes(settings["encrypted_text"], encrypted_text)
            print(f"Зашифрованный текст: {encrypted_text}")

        case Option.DECRYPT_TEXT.value:
            decrypted_text = decrypt_text(read_bytes(settings["encrypted_text"]), read_bytes(settings["symmetric_key"]))
            save_text(settings["decrypted_text"], decrypted_text)
            print(f"Дешифрованный текст: {decrypted_text}")

        case Option.ENCRYPT_SYMMETRIC_KEY.value:
            encrypted_symmetric_key = encrypt_key(read_bytes(settings["symmetric_key"]),
                                                  read_public_key(settings["public_key"]))
            save_bytes(settings["encrypted_symmetric_key"], encrypted_symmetric_key)

        case Option.DECRYPT_SYMMETRIC_KEY.value:
            decrypted_symmetric_key = decrypt_key(read_bytes(settings["encrypted_symmetric_key"]),
                                                  read_private_key(settings["private_key"]))
            save_symmetric_key(settings["decrypted_symmetric_key"], decrypted_symmetric_key)
        case _:
            print("Не выбрана подходящяя опция")
