try:  # Do this in case of an incorrect input
    # Input block
    a = int(input('Type first angle: '))
    b = int(input('Type second angle: '))
    c = int(input('Type third angle: '))
    # In triangle sum of angles must be equal 180
    if a + b + c == 180:
        print('Your triangle exists!')
    else:
        print('Your triangle is impossible(')
except ValueError:
    print('Stop crushing my program!!')
