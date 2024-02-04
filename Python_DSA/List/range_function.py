num = list(range(10))
print(num)
print(num[2])

num = list(range(5, 11))
print(num)

num = list(range(1, 10, 2))
print(num)

squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
