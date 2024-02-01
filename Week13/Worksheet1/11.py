from Queueses import Queue


a = 'EAS*Y*QUE***ST***IO*N***'
q = Queue()
for i in a:
    if i == '*':
        print(q.dequeue(), end="")
    else:
        q.enqueue(i)