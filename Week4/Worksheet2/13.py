try:  # Do this in case of an incorrect input
    print(int(input()) >= 18)  # Input True if they can vote, False if cannot
except ValueError:
    print('Stop crushing my program!!')
