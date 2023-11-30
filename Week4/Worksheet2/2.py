try:  # Do this in case of an incorrect input
    # Input block
    a = int(input())
    b = int(input())
    # Returning the result
    if a == b:
        print(f'{a} = {b}')
    else:
        print(f'{max(a, b)} > {min(a, b)}')
except ValueError:
    print('Something went wrong - try again')