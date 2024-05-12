import os

from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def generate_symmetric_key(key_length: int) -> bytes:
    symmetric_key = os.urandom(key_length)
    return symmetric_key


def encrypt_text(text: str, symmetric_key: bytes) -> bytes:
    padder = PKCS7(128).padder()
    b_text = bytes(text, 'UTF-8')
    padded_text = padder.update(b_text) + padder.finalize()
    iv = os.urandom(8)
    cipher = Cipher(algorithms.CAST5(symmetric_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
    return iv + encrypted_text


def decrypt_text(encrypted_text: bytes, symmetric_key: bytes) -> str:
    iv = encrypted_text[:8]
    encrypted_text = encrypted_text[8:]
    cipher = Cipher(algorithms.CAST5(symmetric_key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
    unpadder = PKCS7(128).unpadder()
    unpadded_decrypted_text = unpadder.update(decrypted_text) + unpadder.finalize()
    final_text = unpadded_decrypted_text.decode('utf-8', errors='ignore')
    return final_text
