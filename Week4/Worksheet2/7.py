try:  # Do this in case of an incorrect input
    a = int(input())
    b = int(input())
    # Check whether the number a is divisible by number b using if statement
    if a % b == 0:
        print(f'{a} is divisible by {b}')
    else:
        print(f'{a} is not divisible by {b}')
except ValueError:
    print('Something went wrong - try again')