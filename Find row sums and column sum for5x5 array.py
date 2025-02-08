# Predefined 5x5 array
arr = [
    [1, 2, 3, 4, 5],       # Row 1: [1, 2, 3, 4, 5]
    [6, 7, 8, 9, 10],      # Row 2: [6, 7, 8, 9, 10]
    [11, 12, 13, 14, 15],  # Row 3: [11, 12, 13, 14, 15]
    [16, 17, 18, 19, 20],  # Row 4: [16, 17, 18, 19, 20]
    [21, 22, 23, 24, 25]   # Row 5: [21, 22, 23, 24, 25]
]

# Initialize lists to store row sums and column sums
row_sums = []            # This will hold the sum of each row
col_sums = [0] * 5      # Start with zero values for the column sums (5 columns in total)
# Example: col_sums = [0, 0, 0, 0, 0]

# Calculating row sums and column sums
for i in range(5):  # Loop through the rows (i goes from 0 to 4)
    row_sum = 0      # Initialize row sum to 0 at the start of each row
    for j in range(5):  # Loop through each column in the row (j goes from 0 to 4)
        row_sum += arr[i][j]  # Add the current element of the row to the row sum
        col_sums[j] += arr[i][j]  # Add the current element to the respective column sum
        # Example: For i = 0, j = 0, arr[0][0] = 1, so row_sum = 0 + 1 = 1
        # Example: col_sums = [1, 0, 0, 0, 0]
    
    row_sums.append(row_sum)  # After the inner loop ends, add the row sum to row_sums
    # Example: After the first row, row_sums = [15] (1+2+3+4+5 = 15)

# Printing the row sums
print("\nRow sums array:", row_sums)
# Output for the above array would be: Row sums array: [15, 40, 65, 90, 105]

# Printing the column sums
print("\nColumn sums array:", col_sums)
# Output for the above array would be: Column sums array: [60, 60, 60, 60, 60]
