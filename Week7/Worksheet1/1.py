def sum_series(n):
    if n <= 0:
        return 0
    return n + sum_series(n - 2)


print(sum_series(int(input('Input n: '))))