my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)

# Adding a new key-value pair
my_dict['gender'] = 'Male'
print(my_dict)  # {'name': 'John', 'age': 26, 'city': 'New York', 'gender': 'Male'}

# Removing a key-value pair
del my_dict['city']
print(my_dict)  # {'name': 'John', 'age': 26, 'gender': 'Male'}
