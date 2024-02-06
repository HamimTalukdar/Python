add = lambda a,b : a+b
result = add(5,2)
print(result)

# or,
print((lambda a,b : a+b) (5,2))

# or,
add = (lambda a,b : a+b) (5,2)
print(add)