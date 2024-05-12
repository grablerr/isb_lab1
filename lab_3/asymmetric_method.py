from typing import Tuple
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes


def generate_asymmetric_keys() -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
    keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = keys
    public_key = keys.public_key()
    return private_key, public_key


def encrypt_key(symmetric_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
    enc_symmetric = public_key.encrypt(symmetric_key,
                                       OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return enc_symmetric


def decrypt_key(enc_symmetric: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
    symmetric_key = private_key.decrypt(enc_symmetric,
                                        OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                             label=None))
    return symmetric_key
