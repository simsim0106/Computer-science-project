def handle_file_not_found(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

# Example usage
print(handle_file_not_found("nonexistent_file.txt"))  # Trying to open a file that doesn't exist