di = {}
try:
    a = int(input('How many values do you want to add to the dictionary: '))
    print('Input to values separated with one space -- example: abc xyz')
    for i in range(a):
        b, c = input().split()
        di[b] = c
    si = {i: di[i] for i in sorted(di)}
    print(si)
except Exception:
    print('Something gone wrong - try again')