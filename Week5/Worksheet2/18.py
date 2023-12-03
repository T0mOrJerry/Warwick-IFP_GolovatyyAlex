try:
    li = []
    for j in range(3):
        di = {}
        a = int(input('How many values do you want to add to the dictionary: '))
        print('Input to values separated with one space -- example: abc xyz')
        for i in range(a):
            b, c = input().split()
            di[b] = c
        li.append(di)
    print(f'Sample dictionaries:\n{li[0]}\n{li[1]}\n{li[2]}')
    fid = {}
    for i in li:
        for j in i:
            fid[j] = i[j]
    print(f'Final dictionary {fid}')
except Exception:
    print('Something gone wrong - try again')