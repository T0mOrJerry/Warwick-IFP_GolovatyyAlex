def unique(li: str):
    li = li[1:-1].split(', ')
    return sorted(list(set(li)))


a = input('type a list in format [a1, a2, a3, ...]: ')
print(unique(a))
