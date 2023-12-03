def dict_inp():
    di = {}
    try:
        a = int(input('How many values do you want to add to the dictionary: '))
        print('Input to values separated with one space -- example: abc xyz')
        for i in range(a):
            b, c = input().split()
            di[b] = c
        return di
    except Exception:
        return {'Error': 'Something gone wrong - try again'}