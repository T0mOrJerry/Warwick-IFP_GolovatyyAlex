# I generate a list, where values are string with the correct, ready for output data
# Then I join the strings inside of array with \n - new string
print('\n'.join([f'Number is: {i} and cube of {i} is: {i ** 3}' for i in
                 range(1, int(input('Input number of terms: ')) + 1)]))
