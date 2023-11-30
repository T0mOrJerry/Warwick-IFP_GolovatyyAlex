from math import prod


try:  # Do this in case of an incorrect input
    # Input block
    li = [int(input()) for i in range(3)]
    # Returning the result
    print(f'sum - {sum(li)}')
    print(f'average - {sum(li) / 3}')
    print(f'prod - {prod(li)}')
    print(f'smallest - {min(li)}')
    print(f'largest - {max(li)}')
except ValueError:
    print('Something went wrong - try again')