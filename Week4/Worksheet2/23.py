mychar = input()  # Input the char
if len(mychar) == 1:
    if mychar.isdigit():  # Check whether it's a digit using string method isdigit()
        print(f'{mychar} char is a digit')
    elif mychar.isalpha():  # Check whether it's an alpha using string method isalpha()
        print(f'{mychar} char is in the alphabet')
    else:
        print(f'{mychar} char is a special char')
else:
    print('Try again! But this time input only ONE char - READ THE CONDITIONS!')