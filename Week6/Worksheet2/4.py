a = input('type a list in format [a1, a2, a3, ...]: ')
li = list(map(int, a[1:-1].split(', ')))
print(list(map(lambda x: x ** 2, li)))
print(list(map(lambda x: x ** 3, li)))