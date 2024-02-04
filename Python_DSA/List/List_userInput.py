n = input("Enter a text of numbers : ")

ar = n.split()
sum = 0

for num in ar:
    sum = sum + int(num)
    
print(sum)