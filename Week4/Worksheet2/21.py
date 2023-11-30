try:  # Do this in case of an incorrect input
    # Input block
    a = int(input('Type first side: '))
    b = int(input('Type second side: '))
    c = int(input('Type third side: '))
    # Using if statement check how many sides are equal
    if a == b and a == c:
        print('Equilateral')
    elif a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Scalene')
except ValueError:
    print('Stop crushing my program!!')
