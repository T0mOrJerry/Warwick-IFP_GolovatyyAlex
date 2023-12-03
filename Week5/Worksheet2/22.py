import sys


li = []
for i in sys.stdin:
    li.append(i.strip())
print(not bool(li))  # Print answering the question "Is this list empty?"
