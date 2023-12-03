a = input('type a list in format [a1, a2, a3, ...]: ')
li = list(map(int, a[1:-1].split(', ')))
li = list(filter(lambda x: x % 2 == 0, li))
print(li)