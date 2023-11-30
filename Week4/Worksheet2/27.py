a = input()  # Input user's mark
# Using several if statements to descript user's mark
if a == 'E':
    print('You got Excellent mark')
elif a == 'V':
    print('You got Very good mark')
elif a == 'G':
    print('You got Good mark')
elif a == 'A':
    print('You got Average mark')
elif a == 'F':
    print('You got Fail mark')
else:  # Case where user typed incorrect data
    print("I don't know what the mark is this")