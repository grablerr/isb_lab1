from typing import Optional

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key


class KeyManager:
    """
    A class for managing cryptographic keys.

    Methods:
        read_private_key: Reads a private key from a file.
        read_public_key: Reads a public key from a file.
        save_public_key: Saves a public key to a file.
        save_private_key: Saves a private key to a file.
        save_symmetric_key: Saves a symmetric key to a file.
    """

    @staticmethod
    def read_private_key(path_to_key: str) -> Optional[rsa.RSAPrivateKey]:
        """
        Reads a private key from a file.

        Args:
            path_to_key (str): The path to the private key file.

        Returns:
            Optional[rsa.RSAPrivateKey]: The private key if successful, None otherwise.
        """
        try:
            with open(path_to_key, 'rb') as pem_in:
                private_bytes = pem_in.read()
            key = load_pem_private_key(private_bytes, password=None)
        except FileNotFoundError:
            key = None
        return key

    @staticmethod
    def read_public_key(path_to_key: str) -> Optional[rsa.RSAPublicKey]:
        """
        Reads a public key from a file.

        Args:
            path_to_key (str): The path to the public key file.

        Returns:
            Optional[rsa.RSAPublicKey]: The public key if successful, None otherwise.
        """
        try:
            with open(path_to_key, 'rb') as pem_in:
                private_bytes = pem_in.read()
            key = load_pem_public_key(private_bytes)
        except FileNotFoundError:
            key = None
        return key

    @staticmethod
    def save_public_key(path_to_save: str, public_key: rsa.RSAPublicKey) -> bool:
        """
        Saves a public key to a file.

        Args:
            path_to_save (str): The path to save the public key.
            public_key (rsa.RSAPublicKey): The public key to save.

        Returns:
            bool: True if the public key was saved successfully, False otherwise.
        """
        saved = True
        try:
            with open(path_to_save, 'wb') as public_out:
                public_out.write(public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
        except FileNotFoundError:
            saved = False
        return saved

    @staticmethod
    def save_private_key(path_to_save: str, private_key: rsa.RSAPrivateKey) -> bool:
        """
        Saves a private key to a file.

        Args:
            path_to_save (str): The path to save the private key.
            private_key (rsa.RSAPrivateKey): The private key to save.

        Returns:
            bool: True if the private key was saved successfully, False otherwise.
        """
        saved = True
        try:
            with open(path_to_save, 'wb') as private_out:
                private_out.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                ))
        except FileNotFoundError:
            saved = False
        return saved

    @staticmethod
    def save_symmetric_key(path: str, key: bytes) -> bool:
        """
        Saves a symmetric key to a file.

        Args:
            path (str): The path to save the symmetric key.
            key (bytes): The symmetric key to save.

        Returns:
            bool: True if the symmetric key was saved successfully, False otherwise.
        """
        saved = True
        try:
            with open(path, 'wb') as key_file:
                key_file.write(key)
        except FileNotFoundError:
            saved = False
        return saved
