"""
                            Chapter 2: Divisibility and Primes
Problem 2.1.26: Make a list of a few odd primes p that can be written as a sum of two squares
(i.e., as $p = x^{2}+y^{2}$); for example, $5 = 2^{2} + 1^{2}$, $13 = 3^{2}+2^{2}$. What is the
remainder when these primes are divided by 4? Prove your guess about the form of the remainder
by first showing that one of $x$ or $y$ must be odd and the other even.

@Author = Hunter Matthews
@Date = 10/25/22

"""

def is_prime(results):
    if results > 1:
        for i in range(2, int(results / 2) + 1):
            if (results % i) == 0:
                break
        else:
            return True


def odd_primes_sum_of_two_squares():
    for i in range(1, 10):
        for j in range(1, 10):
            results = (i ** 2) + (j ** 2)
            flag = is_prime(results)
            if flag is True:
                print(f"{i} ** 2 + {j} ** 2 = {results} <- which is prime")
                print(f"remainder when divided by 4: {results % 4}")


if __name__ == "__main__":
    odd_primes_sum_of_two_squares()
