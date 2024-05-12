from typing import Optional

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key


def read_private_key(path_to_key: str) -> Optional[rsa.RSAPrivateKey]:
    try:
        with open(path_to_key, 'rb') as pem_in:
            private_bytes = pem_in.read()
        key = load_pem_private_key(private_bytes, password=None)
    except FileNotFoundError:
        key = None
    finally:
        return key


def read_public_key(path_to_key: str) -> Optional[rsa.RSAPublicKey]:
    try:
        with open(path_to_key, 'rb') as pem_in:
            private_bytes = pem_in.read()
        key = load_pem_public_key(private_bytes, password=None)
    except FileNotFoundError:
        key = None
    finally:
        return key


def save_public_key(path_to_save: str, public_key: rsa.RSAPublicKey) -> bool:
    saved = True
    try:
        with open(path_to_save, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except FileNotFoundError:
        saved = False
    finally:
        return saved


def save_private_key(path_to_save: str, private_key: rsa.RSAPrivateKey) -> bool:
    saved = True
    try:
        with open(path_to_save, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
    except FileNotFoundError:
        saved = False
    finally:
        return saved
