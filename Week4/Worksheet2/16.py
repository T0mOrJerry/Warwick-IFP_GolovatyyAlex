try:  # Do this in case of an incorrect input
    li = [int(input()) for i in range(3)]  # With list generator create list with 3 inputted values
    print(max(li))
except ValueError:
    print('Stop crushing my program!!')
