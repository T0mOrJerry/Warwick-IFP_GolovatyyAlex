import sys

# Creating a list of objects to operate with.
# In each line type a string, when you want to finish press CTRL+D
li = [i.strip() for i in sys.stdin]
# Filtering strings in the list by stated condition using iterator filter
li = list(filter(lambda x: len(x) >= 2 and x[0] == x[-1], li))
print(f'There are {len(li)} strings, which suits the condition')  # Return the amount of suitable strings
