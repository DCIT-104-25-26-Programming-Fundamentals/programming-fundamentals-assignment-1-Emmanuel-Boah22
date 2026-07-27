# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_numbers():
    """Reads N numbers from the user and returns them as a list.
    Returns None if N is not a positive integer."""
    n = int(input("How many numbers? "))
    if n <= 0:
        print("Error: N must be a positive integer.")
        return None
    return [int(input(f"Enter number {i}: ")) for i in range(1, n + 1)]


def calc_sum(numbers):
    """Returns the sum of the list of numbers using a loop."""
    total = 0
    for num in numbers:
        total += num
    return total


def calc_average(numbers):
    """Returns the average (mean) of the list of numbers using a loop."""
    return calc_sum(numbers) / len(numbers)


def calc_max(numbers):
    """Returns the maximum value in the list using a loop."""
    max_val = numbers[0]
    for num in numbers:
        max_val = num if num > max_val else max_val
    return max_val


def calc_min(numbers):
    """Returns the minimum value in the list using a loop."""
    min_val = numbers[0]
    for num in numbers:
        min_val = num if num < min_val else min_val
    return min_val


def display_results(numbers):
    """Computes and prints Sum, Average, Maximum, and Minimum."""
    print("\nResults:")
    print(f"  Sum:     {calc_sum(numbers)}")
    print(f"  Average: {calc_average(numbers)}")
    print(f"  Maximum: {calc_max(numbers)}")
    print(f"  Minimum: {calc_min(numbers)}")


def main():
    numbers = read_numbers()
    if numbers is None:
        return
    display_results(numbers)


if __name__ == "__main__":
    main()
