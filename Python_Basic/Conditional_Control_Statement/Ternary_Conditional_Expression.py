'''A concise way to express a conditional statement is by using the ternary conditional expression.'''

b = 8
result = "even" if b % 2 == 0 else "odd"
print(f"b is {result}")

num1 = 10
num2 = 20

print(">>>", num1 if num1>num2 else num2)

print(num1 if num1<num2 else num2)