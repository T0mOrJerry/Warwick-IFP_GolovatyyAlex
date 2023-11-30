while True:  # The program will be executing until a correct value is inputted
    a = int(input())  # input the number of the day
    # Using several if statement to return a name of the inputted day
    if a == 1:
        print('Monday')
        break  # If the user gets the answer program stops
    elif a == 2:
        print('Tuesday')
        break
    elif a == 3:
        print('Wednesday')
        break
    elif a == 4:
        print('Thursday')
        break
    elif a == 5:
        print('Friday')
        break
    elif a == 6:
        print('Saturday')
        break
    elif a == 7:
        print('Sunday')
        break