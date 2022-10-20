"""
                            Chapter 0: Introduction
Problem #0.12: Write a computer program to find integer solutions to the
equation (x ** y)(y ** z) = z ** x. Are there infinitely many solutions?

@Author = Hunter Matthews
@Date = 10/20/22

"""

# Yes, this is ugly. Yes, there are infinitely many solutions (see https://math.stackexchange.com/questions/2403217/infinitely-many-solutions-to-axby-cz-for-given-x-y-z-in-mathbbn?rq=1)
def integer_solutions():
    for i in range(0, 5):
        for j in range(0, 5):
            for k in range(0, 5):
                for a in range(0, 5):
                    for b in range(0, 5):
                        for c in range(0, 5):
                            left = (a ** j) * (b ** k)
                            right = c ** i
                            if left == right:
                                print(f"({a} ** {j}) * ({b} ** {k}) = {c} ** {i} (i.e. {left} = {right})")


if __name__ == "__main__":
    integer_solutions()
