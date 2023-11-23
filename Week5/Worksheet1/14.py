# A recursive function for counting factorial
def fact(n):
    if n == 1:
        return 1  # Creating a breakpoint
    return n * fact(n - 1)  # The body of the algorythm


print(fact(int(input())))
