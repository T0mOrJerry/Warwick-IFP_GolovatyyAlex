try:  # Do this in case of an incorrect input
    m = int(input())
    if m == 0:  # We cannot divide by zero
        print(0)
    else:
        print(m // abs(m))  # Fast&Short!
except ValueError:
    print('Stop crushing my program!!')
