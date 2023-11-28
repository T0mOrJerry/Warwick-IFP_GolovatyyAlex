import sys

# Creating a list of objects to operate with.
# In each line type a number, when you want to finish press CTRL+D
li = [int(i) for i in sys.stdin]
print(sorted(li))  # Return the sorted list using built in function sorted()
