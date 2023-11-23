s = 0
for i in range(1, 100, 2):  # Initialising a for loop with a step 2 to take only odd numbers
    s += i  # Add a nuw number to the sum variable
print(s)  # Printing the result
i = 0
while i < 20:  # Initialising a while loop which will stop when counter==20
    i += 1
    print(i, end="\t")
    if i % 5 == 0:
        print()
print()
for i in range(1, 21):  # Initilising for loop with a range [1, 20]
    print(i, end="\t")
    if i % 5 == 0:
        print()
