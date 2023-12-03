# Generate list of odd number using step in range
li = [i for i in range(1, int(input('Input number of terms: '))*2, 2)]
print('The odd numbers are:', *li)  # Print all values of list joined by space
# Using build-in function sum calculate sum of those numbers
print(f'The Sum of odd Natural Number up to {len(li)} terms: {sum(li)}')
