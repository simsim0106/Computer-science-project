def handle_module_not_found(module_name):
    try:
        __import__(module_name)
        return f"Module '{module_name}' was successfully imported."
    except ModuleNotFoundError:
        return f"Error: The module '{module_name}' was not found. Please ensure it is installed."

# Example usage
print(handle_module_not_found("numpy"))
print(handle_module_not_found("nonexistent_module"))  # Non-existent module