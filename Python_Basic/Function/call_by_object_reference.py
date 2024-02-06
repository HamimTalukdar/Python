def modify_list(my_list):
    print("Inside the function, before modification:", my_list)
    my_list.append(42)
    print("Inside the function, after modification:", my_list)

# Calling the function
original_list = [1, 2, 3]
modify_list(original_list)

# Outside the function, the original list is modified
print("Outside the function:", original_list)
