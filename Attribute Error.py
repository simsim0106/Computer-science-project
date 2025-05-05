class SampleClass:
    def __init__(self):
        self.name = "Rigel"

def handle_attribute_error(obj, attribute):
    try:
        return getattr(obj, attribute)
    except AttributeError:
        return f"Error: '{attribute}' attribute does not exist in {type(obj).__name__}."

# Example usage
obj = SampleClass()

print(handle_attribute_error(obj, "name"))
print(handle_attribute_error(obj, "age"))