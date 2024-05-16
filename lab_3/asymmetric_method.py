from typing import Tuple
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes


class AsymmetricEncryptionManager:
    """
    A class for asymmetric encryption operations.

    Methods:
        generate_asymmetric_keys: Generates RSA asymmetric keys.
        encrypt_key: Encrypts a symmetric key using RSA public key.
        decrypt_key: Decrypts an encrypted symmetric key using RSA private key.
    """

    @staticmethod
    def generate_asymmetric_keys() -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
        """
        Generates RSA asymmetric keys.

        Returns:
            Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]: The generated private and public keys.
        """
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private_key = keys
        public_key = keys.public_key()
        return private_key, public_key

    @staticmethod
    def encrypt_key(symmetric_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        """
        Encrypts a symmetric key using RSA public key.

        Args:
            symmetric_key (bytes): The symmetric key to be encrypted.
            public_key (rsa.RSAPublicKey): The RSA public key.

        Returns:
            bytes: The encrypted symmetric key.
        """
        enc_symmetric = public_key.encrypt(
            symmetric_key,
            OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        return enc_symmetric

    @staticmethod
    def decrypt_key(enc_symmetric: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        """
        Decrypts an encrypted symmetric key using RSA private key.

        Args:
            enc_symmetric (bytes): The encrypted symmetric key.
            private_key (rsa.RSAPrivateKey): The RSA private key.

        Returns:
            bytes: The decrypted symmetric key.
        """
        symmetric_key = private_key.decrypt(
            enc_symmetric,
            OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        return symmetric_key
