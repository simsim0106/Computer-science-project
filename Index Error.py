def handle_index_error(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range for the list."

# Example usage
sample_list = [10, 20, 30]

print(handle_index_error(sample_list, 1))
print(handle_index_error(sample_list, 5))