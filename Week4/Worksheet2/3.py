try:  # Do this in case of an incorrect input
    # Input block
    name = input('Type your name: ')
    a = int(input('Type your first grade: '))
    b = int(input('Type your second grade: '))
    c = int(input('Type your third grade: '))
    av = sum([a, b, c]) / 3  # Finding the average
    # Understand which grade a student got
    if av >= 70:
        print(f'{name} is Approved')
    elif 40 <= av < 70:
        print(f'{name} has a resit')
    else:
        print(f'{name} is Failed')
except ValueError:
    print('Something went wrong - try again')