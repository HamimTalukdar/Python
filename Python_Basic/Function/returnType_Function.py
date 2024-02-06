def add_numbers(a: int, b: int) -> int:
    result = a + b
    return result

a = add_numbers(2,3)

print("Result: ", a)

# or,
def add(a,b):
    return a+b
    
result = add(20, 30)
print("Result: ",result)

# or,
def large(a,b):
    if a>b:
        return a
    else:
        return b
    
result = large(20, 30)
print("Result: ",result)

# or,
def large(a,b):
    if a>b:
        return a
    else:
        return b
    
maximum = large
print("Result: ",maximum(20, 30))

