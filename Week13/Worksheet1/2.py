from Stacks import Stack


def exchange(s1: Stack, s2: Stack):
    s2.push(s1.pop())


st1 = Stack()
st1.push(1)
st1.push(2)
st1.push(3)
st2 = Stack()
st2.push(4)
st2.push(5)
st2.push(6)
print(st1, st2)
exchange(st1, st2)
print(st1, st2)