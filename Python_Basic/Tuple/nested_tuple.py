# Creating a nested tuple
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Accessing elements in a nested tuple
print(nested_tuple[0])           # (1, 2, 3)
print(nested_tuple[0][1])        # 2
print(nested_tuple[1][2])        # 6

# Slicing a nested tuple
sliced_tuple = nested_tuple[1:]
print(sliced_tuple)
# ((4, 5, 6), (7, 8, 9))

# Modifying a nested tuple (tuples are immutable, so you need to create a new tuple)
modified_tuple = nested_tuple + ((10, 11, 12),)
print(modified_tuple)
# ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12))
