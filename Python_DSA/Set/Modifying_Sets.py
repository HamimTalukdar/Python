my_set = {1, 2, 3}

# Adding elements
my_set.add(4)
print(my_set)

my_set.update({5, 6, 7})
print(my_set)

# Removing elements
my_set.remove(3)
print(my_set)

my_set.discard(2)  # Discard doesn't raise an error if the element is not present
print(my_set)

my_set.pop()       # Remove and return an arbitrary element
print(my_set)  # {4, 5, 6, 7}
