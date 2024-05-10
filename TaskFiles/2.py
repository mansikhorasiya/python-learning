def input_matrix():
    matrix = []
    print("Enter the elements of the matrix (3x3)")
    for i in range(3):
        row = []
        for j in range(3):
            element = int(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def multiply_matrices(matrix1, matrix2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def display_matrix(matrix):
    for row in matrix:
        print(row)

print("Enter elements for first matrix")
matrix1 = input_matrix()

print("\nEnter elements for second matrix")
matrix2 = input_matrix()

result_matrix = multiply_matrices(matrix1, matrix2)

print("\nThe result of matrix multiplication is:")
display_matrix(result_matrix)
