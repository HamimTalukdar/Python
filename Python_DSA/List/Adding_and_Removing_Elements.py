my_list = [1, 2, 3, 4, 5]
my_list[2] = 10
print(my_list)  # [1, 2, 10, 4, 5]

# Append element to the end
my_list.append(6)
print(my_list)  # [1, 2, 10, 4, 5, 6]

# Insert element at a specific index
my_list.insert(2, 7)
print(my_list)  # [1, 2, 7, 10, 4, 5, 6]

# Remove element by value
my_list.remove(10)
print(my_list)  # [1, 2, 7, 4, 5, 6]

# Remove element by index
removed_value = my_list.pop(3)
print(my_list)       # [1, 2, 7, 5, 6]
print(removed_value)  # 4
