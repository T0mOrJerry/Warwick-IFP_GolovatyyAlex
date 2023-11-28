import sys
from math import prod

# Creating a list of objects to operate with.
# In each line type a number, when you want to finish press CTRL+D
li = [int(i) for i in sys.stdin]
print(f'The sum of numbers in the list is {sum(li)}')  # Return the sum of items using build in function sum()
# Return the product of items using function prod() from module math
print(f'The product of numbers in the list is {prod(li)}')
