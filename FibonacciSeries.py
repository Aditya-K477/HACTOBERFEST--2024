# Function to generate Fibonacci series
def fibonacci(n):
    fib_sequence = [0, 1]  # First two numbers of the series
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        for i in range(2, n):
            next_number = fib_sequence[-1] + fib_sequence[-2]  # Sum of the last two numbers
            fib_sequence.append(next_number)
        return fib_sequence

# Number of terms
n_terms = int(input("Enter the number of terms: "))

# Generating and printing Fibonacci series
fib_series = fibonacci(n_terms)
print(f"Fibonacci series up to {n_terms} terms: {fib_series}")
