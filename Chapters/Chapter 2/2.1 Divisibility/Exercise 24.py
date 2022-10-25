"""
                        Chapter 2: Divisibility and Primes
Problem 2.1.24: We want to generalize the results of the previous two exercises. Fix an
integer m between 5 and 20 and make a table of values n ** m - n for different n, say
n in the range 2 through 25. Does m divide all of these? Do this for all m satisfying
6 <= m <= 20. Make a reasonable conjecture about the numbers m for which n ** m - n
is always divisible by m. Can you prove your conjecture?

@Author = Hunter Matthews
@Date = 10/25/22

"""


def does_m_divide():
    for m in range(2, 25):
        for n in range(5, 20):
            result = (n ** m) - n
            if result % m == 0:
                print(f"{m} divides ({n} ** {m}) - {n} = {result}")


if __name__ == "__main__":
    does_m_divide()
