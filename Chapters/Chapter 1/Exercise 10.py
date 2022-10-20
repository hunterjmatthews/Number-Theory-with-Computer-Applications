"""
                            Chapter 0: Introduction
Problem #0.10: Write a computer program to verify Fermat's conjecture
about the representation of natural numbers as sums of polygonal numbers.

@Author = Hunter Matthews
@Date = 10/20/22

"""


# Verifies Fermat's conjecture for a given two numbers 's' and 'x'
def fermat_polygonal(s, x, n=0, a=[]):
    y = ~n * (~-n - n * s / 2)
    if x < y:
        return (x < 1) * a * (len(a) <= s)
    else:
        return fermat_polygonal(s, x, n + 1, a) or fermat_polygonal(s, x - y, n, a + [y])


# Encapsulates the program’s primary behavior.
if __name__ == "__main__":
    print(fermat_polygonal(6, 43))
