# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


# PART A — Single Table
def print_single_table():
    """Asks the user for a number and prints its multiplication table from 1 to 12."""
    num_user = input("Enter a number: ")
    num = int(num_user)

    if num <= 0:
        print("Error: N must be a positive integer.")
        return

    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        result = num * i
        print(f"{num}  x  {i:2d}  =  {result}")


# PART B — Tables from 1 to N
def print_tables_1_to_n():
    """Asks the user for N and prints multiplication tables for every number from 1 to N."""
    n_str = input("Enter a number N: ")
    n = int(n_str)

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    for num in range(1, n + 1):
        if num > 1:
            print("-" * 27)
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, 13):
            result = num * i
            print(f"{num}  x  {i:2d}  =  {result}")


# Main Program
def main():
    print("PART A — Single Multiplication Table")
    print("=" * 40)
    print_single_table()

    print("\n\nPART B — Tables from 1 to N")
    print("=" * 40)
    print_tables_1_to_n()


if __name__ == "__main__":
    main()
