import os

from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricEncryptionManager:
    """
    A class for symmetric encryption operations.

    Methods:
        generate_symmetric_key: Generates a symmetric key.
        encrypt_text: Encrypts text using a symmetric key.
        decrypt_text: Decrypts text using a symmetric key.
    """

    @staticmethod
    def generate_symmetric_key(key_length: int) -> bytes:
        """
        Generates a symmetric key of the specified length.

        Args:
            key_length (int): The length of the symmetric key in bytes.

        Returns:
            bytes: The generated symmetric key.
        """
        symmetric_key = os.urandom(key_length)
        return symmetric_key

    @staticmethod
    def encrypt_text(text: str, symmetric_key: bytes) -> bytes:
        """
        Encrypts the given text using the provided symmetric key.

        Args:
            text (str): The text to encrypt.
            symmetric_key (bytes): The symmetric key used for encryption.

        Returns:
            bytes: The encrypted text.
        """
        padder = PKCS7(128).padder()
        b_text = bytes(text, 'UTF-8')
        padded_text = padder.update(b_text) + padder.finalize()
        iv = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
        return iv + encrypted_text

    @staticmethod
    def decrypt_text(encrypted_text: bytes, symmetric_key: bytes) -> str:
        """
        Decrypts the given encrypted text using the provided symmetric key.

        Args:
            encrypted_text (bytes): The text to decrypt.
            symmetric_key (bytes): The symmetric key used for decryption.

        Returns:
            str: The decrypted text.
        """
        iv = encrypted_text[:8]
        encrypted_text = encrypted_text[8:]
        cipher = Cipher(algorithms.CAST5(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
        unpadder = PKCS7(128).unpadder()
        unpadded_decrypted_text = unpadder.update(decrypted_text) + unpadder.finalize()
        final_text = unpadded_decrypted_text.decode('utf-8', errors='ignore')
        return final_text
