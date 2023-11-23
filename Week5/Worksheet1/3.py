li = []
a = int(input())
while a != 0:  # Collecting data
    li.append(a)
    a = int(input())
s = 0
for i in li:  # Counting the sum of data
    s += i
print(s / len(li))  # Counting the average
