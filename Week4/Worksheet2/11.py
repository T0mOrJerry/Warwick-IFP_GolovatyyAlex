try:  # Do this in case of an incorrect input
    a = int(input())
    if a == 0:
        print("It's zero")
    elif a > 0:
        print("Positive")
    else:
        print("Negative")
except ValueError:
    print('Stop crushing my program!')
