try:  # Do this in case of an incorrect input
    year = int(input("Input year"))
    # Check whether it's a leap year using if statement
    if year % 400 == 0:
        print('Leap')
    elif year % 100 == 0:
        print('Not leap')
    elif year % 4 == 0:
        print('Leap')
    else:
        print('Not leap')
except ValueError:
    print('Stop crushing my program!')