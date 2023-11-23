# Input the values
a = int(input())
b = int(input())
c = int(input())
aver = int(input())
# Calculate the final grade
grade = (a + 2 * b + 3 * c + aver)/7
# Estimate the grade and print
if grade >= 9:
    print('A')
elif grade >= 7.5:
    print('B')
elif grade >= 6:
    print('C')
elif grade >= 4:
    print('D')
else:
    print('E')