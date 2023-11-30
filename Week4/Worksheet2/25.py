try:  # Do this in case of an incorrect input
    # Input block
    a = int(input('Type cost: '))
    b = int(input('Type selling price: '))
    dif = b - a  # Estimate what difference is between selling price and cost
    if dif < 0:  # Distinguish whether difference is positive or negative
        print(f'Profit is £{dif}')
    elif dif > 0:
        print(f'Loss is £{dif}')
    else:
        print('No losses or profits')
except ValueError:
    print('Stop crushing my program!!')
