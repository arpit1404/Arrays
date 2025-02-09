# Function to take a 3x3 matrix as input from the user
def input_matrix(name):
    print(f"Enter the elements of {name} matrix row-wise:")  # Prompting the user to enter matrix row by row
    matrix = []  # Initialize an empty list to store the matrix

    # Loop to take input for 3 rows
    for i in range(3):
        row = list(map(int, input().split()))  # Read user input, split it by spaces, convert to integers, and store as a list
        matrix.append(row)  # Add the row to the matrix
    
    return matrix  # Return the final 3x3 matrix


# Example Input for input_matrix("first"):
# sql
# Copy
# Edit
# Enter the elements of first matrix row-wise:
# 1 2 3
# 4 5 6
# 7 8 9
# After input, matrix1 looks like:
# python
# Copy
# Edit
# matrix1 = [
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9]
# ]

# Function to multiply two 3x3 matrices
def multiply_matrices(matrix1, matrix2):
    # Initialize a 3x3 result matrix filled with zeros
    result = [[0] * 3 for _ in range(3)]

    # Iterate through rows of the first matrix
    for i in range(3):  
        # Iterate through columns of the second matrix
        for j in range(3):  
            # Perform dot product between row of first matrix and column of second matrix
            for k in range(3):  
                result[i][j] += matrix1[i][k] * matrix2[k][j]  # Multiply and accumulate the sum

    return result  # Return the resultant matrix after multiplication

# Example Input for input_matrix("second"):
# sql
# Copy
# Edit
# Enter the elements of second matrix row-wise:
# 9 8 7
# 6 5 4
# 3 2 1
# After input, matrix2 looks like:
# python
# Copy
# Edit
# matrix2 = [
#     [9, 8, 7], 
#     [6, 5, 4], 22 44 55 
#     [3, 2, 1]
# ]
# Step-by-Step Multiplication
# Matrix multiplication formula:

# Taking input for both matrices
matrix1 = input_matrix("first")  # Get the first 3x3 matrix from user
matrix2 = input_matrix("second")  # Get the second 3x3 matrix from user

# Multiplying matrices
result_matrix = multiply_matrices(matrix1, matrix2)  # Call the function to multiply the matrices

# Display the result
print("Resultant Matrix after Multiplication:")
for row in result_matrix:  # Iterate through each row of the resulting matrix
    print(" ".join(map(str, row)))  # Convert numbers to strings and join them with spaces for a clean display


# Resultant Matrix after Multiplication:
# 30 24 18
# 84 69 54
# 138 114 90