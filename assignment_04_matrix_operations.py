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

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(name="matrix"):
    """Read an M x N matrix from the user."""
    rows = int(input(f"Enter rows for {name}: "))
    cols = int(input(f"Enter columns for {name}: "))
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i + 1}: ").split()))
        matrix.append([int(x) if x.is_integer() else x for x in row])
    return matrix


def print_matrix(matrix, title="Matrix"):
    """Display a matrix in aligned grid format."""
    print(f"\n{title}:")
    widths = [max(len(str(row[c])) for row in matrix)
              for c in range(len(matrix[0]))]
    for row in matrix:
        print("  ".join(str(val).rjust(widths[i])
              for i, val in enumerate(row)))


def transpose_matrix():
    """Part A: Transpose a matrix."""
    print("\n--- Part A: Transpose a Matrix ---")
    m = read_matrix()
    rows, cols = len(m), len(m[0])
    result = [[m[i][j] for i in range(rows)] for j in range(cols)]
    print_matrix(m, "Original Matrix")
    print_matrix(result, "Transposed Matrix")


def add_matrices():
    """Part B: Add two matrices of the same size."""
    print("\n--- Part B: Add Two Matrices ---")
    a = read_matrix("Matrix A")
    b = read_matrix("Matrix B")
    result = [[a[i][j] + b[i][j]
               for j in range(len(a[0]))] for i in range(len(a))]
    print_matrix(a, "Matrix A")
    print_matrix(b, "Matrix B")
    print_matrix(result, "Sum (A + B)")


def multiply_matrices():
    """Part C: Multiply matrix A (M x N) by matrix B (N x P)."""
    print("\n--- Part C: Multiply Two Matrices ---")
    a = read_matrix("Matrix A")
    b = read_matrix("Matrix B")
    rows_a, cols_a, cols_b = len(a), len(a[0]), len(b[0])

    result = [[sum(a[i][k] * b[k][j] for k in range(cols_a))
               for j in range(cols_b)] for i in range(rows_a)]

    print_matrix(a, "Matrix A")
    print_matrix(b, "Matrix B")
    print_matrix(result, "Product (A x B)")


def main():
    transpose_matrix()
    add_matrices()
    multiply_matrices()


if __name__ == "__main__":
    main()
