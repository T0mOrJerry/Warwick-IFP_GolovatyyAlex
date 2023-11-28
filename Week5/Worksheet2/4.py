import sys

# Creating a list of objects to operate with.
# In each line type a number, when you want to finish press CTRL+D
li = [int(i) for i in sys.stdin]
print(f'The larger number is {min(li)}')  # Return the largest number in the list using build in function min()
