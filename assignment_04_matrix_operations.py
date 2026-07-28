# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

# =============================================================================
# YOUR CODE BELOW
# =============================================================================


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:>5}", end=" ")
        print()
    print()


def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            raw_row = input(f"Enter row {i + 1}: ").strip()
            values = raw_row.split()
            if len(values) != cols:
                print(f"Please enter exactly {cols} values.")
                continue

            try:
                row = [int(value) for value in values]
            except ValueError:
                print("Please enter integers only.")
            else:
                matrix.append(row)
                break
    return matrix


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)

    return result


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []

    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(matrix1[r][c] + matrix2[r][c])
        result.append(new_row)

    return result


def multiply_matrices(matrix1, matrix2):
    rows_a = len(matrix1)
    cols_a = len(matrix1[0])
    rows_b = len(matrix2)
    cols_b = len(matrix2[0])

    if cols_a != rows_b:
        raise ValueError("Number of columns in A must equal number of rows in B.")

    result = []
    for r in range(rows_a):
        new_row = []
        for c in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix1[r][k] * matrix2[k][c]
            new_row.append(total)
        result.append(new_row)

    return result


def main():
    print("PART A: Transpose")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    transposed = transpose(matrix)
    print("Transposed Matrix:")
    print_matrix(transposed)

    print("PART B: Add Two Matrices")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Matrix 1:")
    matrix1 = read_matrix(rows, cols)
    print("Matrix 2:")
    matrix2 = read_matrix(rows, cols)
    result_add = add_matrices(matrix1, matrix2)
    print("Sum of Matrices:")
    print_matrix(result_add)

    print("PART C: Multiply Two Matrices")
    rows_a = int(input("Enter rows for Matrix A: "))
    cols_a = int(input("Enter columns for Matrix A: "))
    print("Matrix A:")
    matrix_a = read_matrix(rows_a, cols_a)

    cols_b = int(input("Enter columns for Matrix B: "))
    print("Matrix B:")
    matrix_b = read_matrix(cols_a, cols_b)

    result_mul = multiply_matrices(matrix_a, matrix_b)
    print("Product of Matrices:")
    print_matrix(result_mul)


if __name__ == "__main__":
    main()
