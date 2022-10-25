"""
                            Chapter 2: Divisibility and Primes
Problem 2.1.25: The Fibonacci numbers are defined by: f_{1} = 1, f_{2} = 1, f_{n} = f_{n-1}+f_{n-2}
Hence, f_{3} = f_{2}+f_{1} = 1 +1 =2, f_{4} = f_{3} + f{2} = 2 + 1 = 3, and so on. Make a table
of the first 50 Fibonacci numbers. Which ones are even? Similarly, identify the multiples
of 3, of 5, and of other odd numbers. Prove your conjecture in a few cases. If m is an odd number,
there may not seem a way to all Fibonacci numbers divisible by m. But in the special case when
m is a Fibonacci number f_{d}, it is possible to find the Fibonacci numbers that are multiples
of f_{d}. Determine the multiples of f_{d} and prove your conjecture.

@Author = Hunter Matthews
@Date = 10/25/22

"""

# Finds the fibonacci numbers from 0 - the given n and appends them to a list.
def find_fibonacci_numbers(n):
    # If the user gives an n less than or equal to 0, return the list element [0].
    if n <= 0:
        return [0]
    fibonacci_sequence = [0, 1]
    # While the length of the list is less than or equal to n...
    while len(fibonacci_sequence) <= n:
        next_value = fibonacci_sequence[len(fibonacci_sequence) - 1] + fibonacci_sequence[len(fibonacci_sequence) - 2]
        fibonacci_sequence.append(next_value)
    print_fibonacci_sequence(fibonacci_sequence)


# Prints the f_{d} along with its Fibonacci number in the list. If the fibonacci number is even, a multiple of 3, or
# a multiple of 5, the print that out as well.
def print_fibonacci_sequence(fibonacci_sequence):
    j = 0
    for i in fibonacci_sequence:
        if i % 2 == 0 and i != 0:
            print(f"f_{j} = {i} <- EVEN")
            j += 1
            continue
        if i % 3 == 0 and i != 0:
            print(f"f_{j} = {i} <- Multiple of 3")
            j += 1
            continue
        if i % 5 == 0 and i != 0:
            print(f"f_{j} = {i} <- Multiple of 5")
            j += 1
            continue
        else:
            print(f"f_{j} = {i}")
            j += 1


if __name__ == "__main__":
    find_fibonacci_numbers(50)
