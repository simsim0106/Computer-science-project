def handle_value_error():
    try:
        num = int("hello")  # Trying to convert a non-numeric string to an integer
    except ValueError as e:
        return f"Error: {e}. Please provide a valid number."

# Example usage
print(handle_value_error())