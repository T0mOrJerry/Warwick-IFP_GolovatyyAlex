from Stacks import Stack


def exchange(s1: Stack, s2: Stack):
    s2.push(s1.pop())


st1 = Stack()
st1.push(23)
st1.push(9)
st1.push(17)
st1.push(4)
print(st1)
st2 = Stack()
for i in range(st1.size()):
    exchange(st1, st2)
print(st2)