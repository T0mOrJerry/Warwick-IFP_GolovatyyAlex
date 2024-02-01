# from Stacks import Stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        return self.stack.append(val)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def multi_pop(self, k):
        if self.is_empty():
            return None
        if k > self.size():
            k = self.size()
        res = []
        for i in range(k):
            res.append(self.stack.pop())
        return res

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return ', '.join(list(map(str, self.stack)))

    def size(self):
        return len(self.stack)


st = Stack()
a = input()
flag = True
for i in a:
    if i in '({[':
        st.push(i)
    else:
        s = st.peek()
        if i == '}' and s == '{' or i == ')' and s == '(' or i == ']' and s == '[':
            st.pop()
        else:
            flag = False
            break
if flag:
    print('Valid')
else:
    print('Invalid')
