class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "I can't divide by zero("


fl = True
calculator = Calculator()
while fl:
    print()
    try:
        menu_choice = int(input(
            'Press 0 if you want to exit\nPress 1 for addition\nPress 2 for subtraction\n'
            'Press 3 for multiplication\nPress 4 for division\n'))
    except ValueError:
        print('Why would you do that?!')
        continue
    if menu_choice == 0:
        fl = False
    else:
        if menu_choice not in [0, 1, 2, 3, 4]:
            print('There is no such choice, try again')
            continue
        try:
            a = float(input('Type first number for operation: '))
            b = float(input('Type second number for operation: '))
        except ValueError:
            print('You have to type a number, try again')
            continue
        if menu_choice == 1:
            print(f'{a} + {b} = {calculator.add(a, b)}')
        elif menu_choice == 2:
            print(f'{a} - {b} = {calculator.sub(a, b)}')
        elif menu_choice == 3:
            print(f'{a} * {b} = {calculator.mult(a, b)}')
        elif menu_choice == 4:
            print(f'{a} / {b} = {calculator.div(a, b)}')

