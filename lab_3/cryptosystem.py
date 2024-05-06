import os

from typing import Tuple

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes


def generate_keys(key_length: int) -> Tuple[bytes, rsa.RSAPrivateKey, rsa.RSAPublicKey]:
    symmetric_key = os.urandom(key_length)
    keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = keys
    public_key = keys.public_key()
    enc_symmetric = public_key.encrypt(symmetric_key,
                                       OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return enc_symmetric, private_key, public_key
