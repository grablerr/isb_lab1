import os

from typing import Tuple
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def generate_keys(key_length: int) -> Tuple[bytes, rsa.RSAPrivateKey, rsa.RSAPublicKey]:
    symmetric_key = os.urandom(key_length)
    keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = keys
    public_key = keys.public_key()
    enc_symmetric = public_key.encrypt(symmetric_key,
                                       OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return enc_symmetric, private_key, public_key


def encrypt_text(text: str, enc_symmetric: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
    symmetric_key = private_key.decrypt(enc_symmetric,
                                        OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                             label=None))
    padder = PKCS7(128).padder()
    b_text = bytes(text, 'UTF-8')
    padded_text = padder.update(b_text) + padder.finalize()
    iv = os.urandom(8)
    cipher = Cipher(algorithms.CAST5(symmetric_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
    return iv + encrypted_text


def decrypt_text(encrypted_text: bytes, enc_symmetric: bytes, private_key: rsa.RSAPrivateKey) -> str:
    symmetric_key = private_key.decrypt(enc_symmetric,
                                        OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                             label=None))
    iv = encrypted_text[:8]
    encrypted_text = encrypted_text[8:]
    cipher = Cipher(algorithms.CAST5(symmetric_key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
    unpadder = PKCS7(128).unpadder()
    unpadded_decrypted_text = unpadder.update(decrypted_text) + unpadder.finalize()
    final_text = unpadded_decrypted_text.decode('utf-8', errors='ignore')
    return final_text
