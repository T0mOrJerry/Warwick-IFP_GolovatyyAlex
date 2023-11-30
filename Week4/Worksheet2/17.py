try:  # Do this in case of an incorrect input
    math = int(input('Input your math mark: '))
    physics = int(input('Input your physics mark: '))
    chemistry = int(input('Input your chemistry mark: '))
    #  If statement with a whole condition
    if (math >= 65 and physics >= 55 and chemistry >= 50) and (math + physics + chemistry >= 190 or math + physics):
        print('You r accepted')
    else:
        print('Study harder')
except ValueError:
    print('Stop crushing my program!!')
