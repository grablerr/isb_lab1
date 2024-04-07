import json


def read_path_file(file_path: str) -> list[str]:
    """
    A method for reading paths from a JSON file
    Parameters: file_path (type str)
    Returns: List[str]
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [data.get("folder", ""), data.get("input_text", ""), data.get("output_text", "")]
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
    except Exception as e:
        print(f"An error occurred: {e}")
