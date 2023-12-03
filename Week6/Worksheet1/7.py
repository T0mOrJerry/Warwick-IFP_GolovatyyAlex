def calc_up(s: str):
    counter = 0
    for i in s:
        if i.isupper():
            counter += 1
    return counter


def calc_low(s: str):
    counter = 0
    for i in s:
        if i.islower():
            counter += 1
    return counter


str_to_calc = input('Input a string: ')
print(f'Number of lower case letters - {calc_low(str_to_calc)}')
print(f'Number of upper case letters - {calc_up(str_to_calc)}')