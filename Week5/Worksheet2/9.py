a = input('Type the frase: ')  # Inputting the frase
li = list(a)  # Creating a list of chars
first = li[0]  # Taking the first char to compare it with others
for i in range(len(li)):
    if i != 0 and li[i] == first:  # compare all the chars with the first
        li[i] = '$'
print(''.join(li))  # Turning the list back into the string
