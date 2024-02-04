# Get user input as a comma-separated string
input_string = input("Enter elements separated by commas: ")

# Convert the input string to a set
user_set = set(map(int, input_string.split(',')))

# Display the resulting set
print("User Set:", user_set)
