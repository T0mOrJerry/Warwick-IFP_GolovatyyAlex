def fall_in_range(t: list[str], n: int):
    t = sorted(t)
    return int(t[0]) <= n < int(t[1])


r = input('Type a range - two numbers divided with space, where first is lesser than the second: ').split()
num = int(input('Type a number you want to check: '))
print(fall_in_range(r, num))