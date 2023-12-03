import sys


li = []
for i in sys.stdin:
    li.append(i.strip())
li = sorted(list(set(li)))
print(*li)
