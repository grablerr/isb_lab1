from constants_and_paths import CPP, JAVA


def get_sequence(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{file_name}' not found")
        return None
    except Exception as e:
        print(f"An error while reading file: {e}")
        return None


def main():
    cpp_sequence = get_sequence(CPP)
    java_sequence = get_sequence(JAVA)
    print(cpp_sequence)
    print(java_sequence)


if __name__ == "__main__":
    main()
