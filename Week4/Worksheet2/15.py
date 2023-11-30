try:  # Do this in case of an incorrect input
    height = float(input())
    # Determine how tall the person is
    if height <= 170:
        print('Halfling!')
    elif 170 < height < 190:
        print('Tall dwarf')
    else:
        print('Ala, Mithrandir!')
except ValueError:
    print('Stop crushing my program!!')
