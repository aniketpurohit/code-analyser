# file_reader.py


def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."


if __name__ == "__main__":
    path = "sample.txt"  # Replace with your file path
    print(read_file(path))
