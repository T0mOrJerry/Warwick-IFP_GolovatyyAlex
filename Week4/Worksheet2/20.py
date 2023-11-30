try:  # Do this in case of an incorrect input
    temperature = int(input())  # Input temperature
    # If block to understand how cold the water is
    if temperature < 0:
        print('Freezing water')
    elif 0 <= temperature < 10:
        print('Very cold water!')
    elif 10 <= temperature < 20:
        print('Cold water')
    elif 20 <= temperature < 30:
        print('Normal')
    elif 30 <= temperature < 40:
        print('Hot water')
    else:
        print('Extremely hot water')
except ValueError:
    print('Stop crushing my program!!')
