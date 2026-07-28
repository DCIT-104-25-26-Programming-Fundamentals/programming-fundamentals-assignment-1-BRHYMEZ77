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

def find_sum(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

def find_average(numbers):
    total = find_sum(numbers)
    return total / len(numbers)

def find_max(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

def find_min(numbers):
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest

def main():
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Error: You must enter a positive number of items.")
        return
    numbers = []
    for _ in range(count):
        num = float(input("Enter a number: "))
        numbers.append(num)

    total = find_sum(numbers)
    average = find_average(numbers)
    biggest = find_max(numbers)
    smallest = find_min(numbers)

    print("Sum:     ", total)
    print("Average: ", average)
    print("Maximum: ", biggest)
    print("Minimum: ", smallest)

if __name__ == "__main__":
    main()