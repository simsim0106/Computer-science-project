def handle_key_error(dictionary, key):
    try:
        return dictionary[key]  
    except KeyError:
        return f"Error: The key '{key}' does not exist in the dictionary."

# Example usage
sample_dict = {"name": "Rigel", "age": 25}

print(handle_key_error(sample_dict, "name"))  
print(handle_key_error(sample_dict, "address"))  