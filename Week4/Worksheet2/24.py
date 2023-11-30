mychar = input()  # Input the char
if len(mychar) == 1:
    if mychar.isalpha():
        if mychar.lower() in 'eyuioa':
            print(f'{mychar} is a vowel')
        else:
            print(f'{mychar} is a consonant')
    else:
        print('Try again! But this time input only letter char - READ THE CONDITIONS!')
else:
    print('Try again! But this time input only ONE char - READ THE CONDITIONS!')