from math import prod


def mult_lst():
    a = input('type a list in format (a1, a2, a3, ...): ')
    a = a[1:-1]
    li = list(map(int, a.split(', ')))
    return prod(li)


print(mult_lst())