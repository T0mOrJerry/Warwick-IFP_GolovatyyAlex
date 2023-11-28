try:
    a = int(input())
    b = int(input())
    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    if b == 0:
        print('Cannot divide by zero')
    else:
        print(f'{a} / {b} = {a / b}')
except Exception:
    print('Something went wrong - try again')