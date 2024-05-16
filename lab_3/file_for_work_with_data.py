import json

from typing import Optional, Dict


class FileManager:
    """
    A class for file management operations.

    Methods:
        read_json: Reads JSON data from a file.
        read_bytes: Reads bytes data from a file.
        save_bytes: Saves bytes data to a file.
        read_text: Reads text data from a file.
        save_text: Saves text data to a file.
    """

    @staticmethod
    def read_json(path_to_data: str) -> Optional[Dict[str, str]]:
        """
        Reads JSON data from a file.

        Args:
            path_to_data (str): The path to the JSON file.

        Returns:
            Optional[Dict[str, str]]: The JSON data as a dictionary if successful, None otherwise.
        """
        try:
            with open(path_to_data, 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = None
        return data

    @staticmethod
    def read_bytes(path_to_data: str) -> Optional[bytes]:
        """
        Reads bytes data from a file.

        Args:
            path_to_data (str): The path to the file.

        Returns:
            Optional[bytes]: The bytes data if successful, None otherwise.
        """
        try:
            with open(path_to_data, 'rb') as f:
                data = f.read()
        except FileNotFoundError:
            data = None
        return data

    @staticmethod
    def save_bytes(path_to_save: str, data: bytes) -> bool:
        """
        Saves bytes data to a file.

        Args:
            path_to_save (str): The path to save the data.
            data (bytes): The bytes data to save.

        Returns:
            bool: True if the data was saved successfully, False otherwise.
        """
        saved = True
        try:
            with open(path_to_save, 'wb') as f:
                f.write(data)
        except FileNotFoundError:
            saved = False
        return saved

    @staticmethod
    def read_text(path_to_text: str) -> Optional[str]:
        """
        Reads text data from a file.

        Args:
            path_to_text (str): The path to the text file.

        Returns:
            Optional[str]: The text data if successful, None otherwise.
        """
        try:
            with open(path_to_text, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            text = None
        return text

    @staticmethod
    def save_text(path_to_save: str, text: str) -> bool:
        """
        Saves text data to a file.

        Args:
            path_to_save (str): The path to save the text.
            text (str): The text data to save.

        Returns:
            bool: True if the text was saved successfully, False otherwise.
        """
        saved = True
        try:
            with open(path_to_save, 'w', encoding='utf-8') as f:
                f.write(text)
        except FileNotFoundError:
            saved = False
        return saved
