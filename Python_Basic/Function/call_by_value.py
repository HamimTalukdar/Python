def modify_value(x):
    print("Inside the function, before modification:", x)
    x = 42
    print("Inside the function, after modification:", x)

# Calling the function
value = 10
modify_value(value)

# Outside the function, the original value remains unchanged
print("Outside the function:", value)
