line = input('Type your sentence: ')  # Inputting the scentence
li = line.split()  # Creating a list, containing all the words of the scentence
unique = list(set(li))  # Creating a list of unique words in our sentence
dict = {}  # Initialising a dictionary for counting
# The folowing loop count the each word in the list of words in sentence
for i in unique:
    dict[i] = li.count(i)
print(dict)  # Outputting the words and their amount
