def square(x) :
    return x*x

num = [1,2,3,4,5]

result = list(map(square, num))
print(result)

# Using lambda with the map function
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))
