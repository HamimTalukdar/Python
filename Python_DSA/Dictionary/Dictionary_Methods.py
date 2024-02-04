my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)

# Get value by key (with default value if key doesn't exist)
print(my_dict.get('name', 'Unknown'))  # John
print(my_dict.get('occupation', 'Unknown'))  # Unknown

# Get keys, values, or key-value pairs
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

# Copy a dictionary
copied_dict = my_dict.copy()

# Clear all items from a dictionary
my_dict.clear()
