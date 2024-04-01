import json


def read_path_file(file_path: str) -> dict:
    """
    A method for reading paths from a JSON file
    Parameters: file_path (type str)
    Returns: dict
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found1.")
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
    except Exception as e:
        print(f"An error occurred: {e}")