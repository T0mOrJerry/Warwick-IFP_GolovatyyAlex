from Queueses import Queue


q = Queue()
for i in range(4):
    q.enqueue(i)

print(q)
print(q.size())

for i in range(3):
    q.dequeue()
print(q.peek())
print(q.is_empty())
q.dequeue()
print(q.is_empty())