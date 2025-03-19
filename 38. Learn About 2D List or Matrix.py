# Creating a 2D List (Matrix)
nums = [
    [5, 20, 3],
    [7, -10, 9]
]

# Finding the number of rows and columns
rows = len(nums)
cols = len(nums[0])  # Non-square matrix

# Printing the matrix
print("Original Matrix:")
for row in nums:
    print(row)

# Sum of all elements in the matrix
matrix_sum = 0
for i in range(rows):
    for j in range(cols):
        matrix_sum += nums[i][j]
print("\nSum of all elements:", matrix_sum)

# Row-wise sum
print("\nRow-wise Sum:")
for i in range(rows):
    row_sum = 0
    for j in range(cols):
        row_sum += nums[i][j]
    print(f"Row {i}: {row_sum}")

# Column-wise sum
print("\nColumn-wise Sum:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += nums[i][j]
    print(f"Column {j}: {col_sum}")

# Upper Triangle (For square matrices)
if rows == cols:
    print("\nUpper Triangle:")
    for i in range(rows):
        for j in range(cols):
            if j >= i:
                print(nums[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()

    # Lower Triangle
    print("\nLower Triangle:")
    for i in range(rows):
        for j in range(cols):
            if j <= i:
                print(nums[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()

    # Diagonal Elements
    print("\nMain Diagonal:")
    for i in range(rows):
        print(nums[i][i], end=" ")
    print()

    print("\nAnti-Diagonal:")
    for i in range(rows):
        print(nums[i][cols - 1 - i], end=" ")
    print()

# Transpose of Matrix (New approach)
print("\nTranspose of the Matrix:")
transposed = [[0] * rows for _ in range(cols)]  # Create a new 2D list initialized with 0s

for i in range(rows):
    for j in range(cols):
        transposed[j][i] = nums[i][j]  # Swap row and column positions

# Printing Transposed Matrix
for row in transposed:
    print(row)
