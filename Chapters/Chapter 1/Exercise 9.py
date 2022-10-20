"""
                            Chapter 0: Introduction
Problem #0.9: Make a list of numbers that can be written as sums of three squares.
Which numbers are not in your list? What can you say about numbers that
are not sums of three squares?

@Author = Hunter Matthews
@Date = 10/20/22

"""


# Legendre's three-square theorem - Finds all numbers 'n' that can be expressed as n = 4^a(8b + 7))
def not_sums_of_three_squares():
    sums = []
    for i in range(0, 10):
        for j in range(0, 10):
            n = (4 ** i) * ((8 * j) + 7)
            sums.append(n)
    return sorted(sums)

# Find all numbers that are sums of three squares.
def sums_of_three_squares():
    sums = []
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                n = i ** 2 + j ** 2 + k ** 2
                sums.append(n)
    return sorted(sums)


# Find all numbers that are not in the list of Legendre numbers.
def not_in_list(sums):
    result = []
    for x in sums:
        if x not in result:
            result.append(x)
    return result

# Encapsulates the program’s primary behavior.
if __name__ == "__main__":
    not_sums = not_sums_of_three_squares()
    sums = sums_of_three_squares()
    result = not_in_list(sums)
    print(result)
    print("\n")
    print(not_sums)
