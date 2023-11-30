f = True  # The program will work until the user input the equation correctly
while f:
    a = input('type an equation in format: +/-a*x**2 +/-b*x +/-c = 0 - ex. 2*x**2 +0*x -1 = 0: ')
    try:  # If something is wrong with the equation format the program will return to the beginning
        li = a.split(' ')
        li = li[:4]
        # Taking the coefficients from inputted line
        a = int(li[0][:-5])
        b = int(li[1][:-2])
        c = int(li[2])
        # Make If system for cases, where some coefficients equal zero
        if a == 0:
            if b == 0:
                if c == 0:
                    print('(-inf; +inf)')
                else:
                    print('No solutions')
            else:
                print((-c) / b)
        else:
            d = b ** 2 - 4 * a * c  # Gain discriminant
            # Process different values for discriminant
            if d < 0:
                print('No solutions in Real')
            elif d == 0:
                print(-b / (2 * a))
            else:
                print((-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a))
        f = False  # End cycle if everything is done correctly
    except IndexError:
        print('Invalid input - try again)))')
    except ValueError:
        print('Invalid input - try again)))')