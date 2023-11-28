# Also, nothing to comment, really
a = input('Type your first string: ')
b = input('Type your second string: ')
if len(a) < 2 or len(b) < 2:
    print('Not enough chars :(')
else:
    print(b[:2] + a[2:] + ' ' + a[:2] + b[2:])