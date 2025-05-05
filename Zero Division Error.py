def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

# Example usage
num1 = 10
num2 = 0

print(safe_divide(num1, num2))
print(safe_divide(num1, 2))