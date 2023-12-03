from DIctionaryInput import dict_inp


di = dict_inp()
user_key = input('Type a key you want to find in the dictionary: ')
if user_key in di:
    print(f'This key is in the dictionary - the value is {di[user_key]}')
else:
    print(f'There are no such key - {user_key}')