# Nothing to comment really.... I'm tired of commenting(((
a = input('Type your string: ')
if len(a) < 2:
    print('Not enough chars :(')
else:
    print(a[:2] + a[-2:])