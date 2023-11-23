a = input('type a list in format [a1, a2, a3]: ')
a = a[1:-1]
li = list(map(int, a.split(', ')))
print(sum(li))