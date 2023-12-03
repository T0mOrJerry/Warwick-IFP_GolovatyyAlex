a = input('type the first list in format [a1, a2, a3, ...]: ')
lia = list(map(int, a[1:-1].split(', ')))
b = input('type the second list in format [a1, a2, a3, ...]: ')
lib = list(map(int, b[1:-1].split(', ')))
print(list(set(lia) & set(lib)))  # In the task said "array" - set is an array
