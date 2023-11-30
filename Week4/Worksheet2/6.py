try:  # Do this in case of an incorrect input
    a = int(input())
    # Check whether the number is odd or even using if statement
    if a % 2 == 0:
        print('Even')
    else:
        print('Odd')
except ValueError:
    print('Something went wrong - try again')