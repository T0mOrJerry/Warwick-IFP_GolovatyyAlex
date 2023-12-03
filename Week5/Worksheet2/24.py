str_to_change = input()
if len(str_to_change) > 1:
    print(str_to_change[-1] + str_to_change[1:-1] + str_to_change[0])
else:
    print(str_to_change)