class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.insert(0, val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return ', '.join(list(map(str, self.items)))

    def size(self):
        return len(self.items)


# q = Queue()
# for i in range(4):
#     q.enqueue(i)
#
# print(q)
# print(q.size())
#
# for i in range(3):
#     q.dequeue()
# print(q.peek())

