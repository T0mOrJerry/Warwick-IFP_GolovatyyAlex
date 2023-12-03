b = int(input('How much values do you want to enter?\n'))
li = [input() for i in range(b)]  # Create an array to store all the inputted values
a = input('Type a value you want to find in the array: ')
if a not in li:  # Check if value was added to the array
    print('Number does not exist in the array')
else:
    print(f'The value is found, it has index - {li.index(a)}')  # Find the index using built-in list method - index
