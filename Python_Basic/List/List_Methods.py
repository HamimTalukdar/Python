my_list = [1, 2, 3]

print(len(my_list)) # Output: 3

my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]

my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]

my_list = [1, 2, 3]
popped_element = my_list.pop()
print(popped_element)  # Output: 3

my_list = [1, 2, 3]
popped_element = my_list.pop(1)
print(popped_element)  # Output: 2

my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1

my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2

my_list = [1, 2, 3, 2]
my_list_2 = my_list.copy()
print(my_list_2)  # Output: [1, 2, 3, 2]

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
