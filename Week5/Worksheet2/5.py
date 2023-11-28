a = input('Type your string: ')
di = {}
li = sorted(list(set(list(a))))  # Creating a sorted list of unique chars in the string
# Count the amount of each unique char in the string ising method count()
for i in li:
    di[i] = a.count(i)
print(di)  # Return the result dictionary
