# Functions & Fibonacci Sequence
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
#We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = []  # Initialize an empty list to store the Fibonacci sequence

    if n <= 1:
        fibonacci_sequence = [0] if n == 1 else []  # If n is 1, sequence starts with 0; if n is 0, sequence is empty
    else:
        a, b = 0, 1  # Initialize the first two terms of the Fibonacci sequence
        fibonacci_sequence = [a, b]  # Append the first two terms to the sequence
        for _ in range(2, n):
            c = a + b  # Calculate the next term in the sequence
            fibonacci_sequence.append(c)  # Append the next term to the sequence
            a, b = b, c  # Update a and b for the next iteration

    return fibonacci_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print("Fibonacci sequence:")
print(fibonacci_sequence)



# Your program should:

# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.

