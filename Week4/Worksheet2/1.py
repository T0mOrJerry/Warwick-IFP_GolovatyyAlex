try:  # Do this in case of an incorrect input
    # Input block
    a = int(input())
    b = int(input())
    # Output block
    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    if b == 0:  # Check division by zero
        print('Cannot divide by zero')
    else:
        print(f'{a} / {b} = {a / b}')
except ValueError:
    print('Something went wrong - try again')