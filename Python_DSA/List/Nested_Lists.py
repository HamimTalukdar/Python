matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0][1])  # 2
print(matrix[2][0])  # 7

for row in matrix:
    for col in row:
        print(col,end=" ")
    print()