try:  # Do this in case of an incorrect input
    print(int(input()) == int(input()))  # Check
except ValueError:
    print('Stop crushing my program!')
