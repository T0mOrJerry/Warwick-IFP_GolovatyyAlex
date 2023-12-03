str_to_change = input()
n = int(input('Type an index of char you want to remove: '))
if n <= len(str_to_change) - 1:
    li = list(str_to_change)
    li.pop(n)
    print(''.join(li))
else:
    print('Index is out of range')
