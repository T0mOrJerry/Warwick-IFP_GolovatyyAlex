while True:  # The program will be executing, until first correct input
    a = input('Type your word: ')  # inputting string
    if len(a) < 3:  # Check weather it's valid
        print('Try again')  # Report an error
    else:
        if a[-3:] == 'ing':  # Check what should we add to string
            a += 'ly'
        else:
            a += 'ing'
        print(a)  # Outputting the result
        break  # Escape the cycle
