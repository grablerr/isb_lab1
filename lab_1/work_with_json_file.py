import json


def get_folder(json_data) -> str:
    return json_data["folder"]


def get_input_text(json_data) -> str:
    return json_data["input_text"]


def get_output_text(json_data) -> str:
    return json_data["output_text"]


def read_path_file(file_path: str) -> list[str]:
    """
    A method for reading paths from a JSON file
    Parameters: file_path (type str)
    Returns: List[str]
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            folder = get_folder(data)
            input_text = get_input_text(data)
            output_text = get_output_text(data)
            return [folder, input_text, output_text]
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
    except Exception as e:
        print(f"An error occurred: {e}")