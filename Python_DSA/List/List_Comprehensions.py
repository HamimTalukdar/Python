num = [1,2,3,4,5]
print(num)

result = [x*x for x in num]
print(result)

num = [1,2,3,4,5]
print(num)
result = list(filter(lambda x : x%2==0, num))
print(result)

# or,
num = [1,2,3,4,5]
print(num)
result = [x for x in num if x%2==0]
print(result)