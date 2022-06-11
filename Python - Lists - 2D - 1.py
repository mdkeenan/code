# 2D Lists

# Creates a 2d list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the second item in the second row in matrix.
print(matrix[2][2])

# For each row in matrix select the item in each row and print it.
for row in matrix:
    for item in row:
        print(item)

# For each row in matrix print index 1.
for row in matrix:
    print(row[1])
