import argparse

from enum import Enum

from asymmetric_method import AsymmetricEncryptionManager
from symmetric_method import SymmetricEncryptionManager
from file_for_work_with_data import FileManager
from file_for_serialization import KeyManager


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

    settings = FileManager.read_json("settings.json")
    if settings is None:
        print("Файл настроек не найден.")
        exit(1)

    match (args.option):
        case Option.GENERATE_SYMMETRIC_KEY.value:
            symmetric_key = SymmetricEncryptionManager.generate_symmetric_key(16)
            KeyManager.save_symmetric_key(settings["symmetric_key"], symmetric_key)
        case Option.GENERATE_ASYMMETRIC_KEYS.value:
            private_key, public_key = AsymmetricEncryptionManager.generate_asymmetric_keys()
            KeyManager.save_public_key(settings["public_key"], public_key)
            KeyManager.save_private_key(settings["private_key"], private_key)

        case Option.ENCRYPT_TEXT.value:
            encrypted_text = SymmetricEncryptionManager.encrypt_text(FileManager.read_text(settings["source_text"]),
                                                                     FileManager.read_bytes(settings["symmetric_key"]))
            FileManager.save_bytes(settings["encrypted_text"], encrypted_text)
            print(f"Зашифрованный текст: {encrypted_text}")

        case Option.DECRYPT_TEXT.value:
            decrypted_text = SymmetricEncryptionManager.decrypt_text(FileManager.read_bytes(settings["encrypted_text"]),
                                                                     FileManager.read_bytes(settings["symmetric_key"]))
            FileManager.save_text(settings["decrypted_text"], decrypted_text)
            print(f"Дешифрованный текст: {decrypted_text}")

        case Option.ENCRYPT_SYMMETRIC_KEY.value:
            encrypted_symmetric_key = AsymmetricEncryptionManager.encrypt_key(
                FileManager.read_bytes(settings["symmetric_key"]),
                KeyManager.read_public_key(settings["public_key"]))
            FileManager.save_bytes(settings["encrypted_symmetric_key"], encrypted_symmetric_key)

        case Option.DECRYPT_SYMMETRIC_KEY.value:
            decrypted_symmetric_key = AsymmetricEncryptionManager.decrypt_key(
                FileManager.read_bytes(settings["encrypted_symmetric_key"]),
                KeyManager.read_private_key(settings["private_key"]))
            KeyManager.save_symmetric_key(settings["decrypted_symmetric_key"], decrypted_symmetric_key)
        case _:
            print("Не выбрана подходящяя опция")
