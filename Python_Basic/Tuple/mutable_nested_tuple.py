mutable_nested_tuple = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

# Modifying an element within a mutable inner tuple
mutable_nested_tuple[0][1] = 10
print(mutable_nested_tuple)
# ([1, 10, 3], [4, 5, 6], [7, 8, 9])
