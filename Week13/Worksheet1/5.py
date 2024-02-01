from Stacks import Stack


def exchange(s1: Stack, s2: Stack):
    s2.push(s1.pop())


st1 = Stack()
st1.push(23)
st1.push(12)
st1.push(8)
st1.push(9)
st1.push(17)
st1.push(4)
print(st1)
storodd = Stack()
storeven = Stack()
for i in range(st1.size()):
    p = st1.peek()
    if p % 2 == 0:
        exchange(st1, storeven)
    else:
        exchange(st1, storodd)
for i in range(storodd.size()):
    exchange(storodd, st1)
for i in range(storeven.size()):
    exchange(storeven, st1)
print(st1)