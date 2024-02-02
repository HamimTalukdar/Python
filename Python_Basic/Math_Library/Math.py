# from math import *

'''max(): Returns the largest item in an iterable or the largest of two or more arguments.'''
# Using max() with numbers
max_num = max(3, 8, 1, 6, 2)
print("Max:", max_num)

# Using max() with an iterable
numbers = [3, 8, 1, 6, 2]
max_num_in_list = max(numbers)
print("Max in list:", max_num_in_list)


'''min(): Returns the smallest item in an iterable or the smallest of two or more arguments.'''
# Using min() with numbers
min_num = min(3, 8, 1, 6, 2)
print("Min:", min_num)

# Using min() with an iterable
numbers = [3, 8, 1, 6, 2]
min_num_in_list = min(numbers)
print("Min in list:", min_num_in_list)


'''abs(): Returns the absolute value of a number.'''
# Using abs() with a number
absolute_value = abs(-5.6)
print("Absolute value:", absolute_value)


'''round(): Rounds a floating-point number to the nearest integer or to the specified number of decimals.'''
rounded_num = round(3.14159)
print("Rounded number:", rounded_num)

rounded_decimal = round(3.14159, 2)
print("Rounded to 2 decimals:", rounded_decimal)


'''sum(): Returns the sum of all elements in an iterable.'''
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("Sum:", total)


'''divmod(): Returns a tuple containing the quotient and the remainder when dividing two numbers.'''
result = divmod(10, 3)
print("Quotient and remainder:", result)  # Output: (3, 1)


'''pow(): Returns the result of raising a number to a specified power.'''
power_result = pow(2, 3)
print("2 raised to the power of 3:", power_result)


'''abs(): Returns the absolute value of a number.'''
absolute_value = abs(-5.6)
print("Absolute value:", absolute_value)
