a = int(input('Type the number: '))
print(' '.join([str(i) for i in range(1, a + 1)]))  # Create a list of first a numbers and join them with spaces
print(sum([i for i in range(1, a + 1)]))  # Create a list of first a numbers and summarize them
