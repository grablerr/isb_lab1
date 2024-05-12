import json
from typing import Optional, Dict


def read_json(path_to_data: str) -> Optional[Dict[str, str]]:
    try:
        with open(path_to_data, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = None
    finally:
        return data


def read_bytes(path_to_data: str) -> Optional[bytes]:
    try:
        with open(path_to_data, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        data = None
    finally:
        return data


def save_bytes(path_to_save: str, data: bytes) -> bool:
    saved = True
    try:
        with open(path_to_save, 'wb') as f:
            f.write(data)
    except FileNotFoundError:
        saved = False
    finally:
        return saved


def read_text(path_to_text: str) -> Optional[str]:
    try:
        with open(path_to_text, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        text = None
    finally:
        return text


def save_text(path_to_save: str, text: str) -> bool:
    saved = True
    try:
        with open(path_to_save, 'w', encoding='utf-8') as f:
            f.write(text)
    except FileNotFoundError:
        saved = False
    finally:
        return saved
