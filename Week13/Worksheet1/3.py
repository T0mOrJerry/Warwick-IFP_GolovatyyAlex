from Stacks import Stack


def exchange(s1: Stack, s2: Stack):
    s2.push(s1.pop())


st1 = Stack()
st1.push(23)
st1.push(9)
st1.push(17)
st1.push(4)
print(st1)
stor1 = Stack()
stor2 = Stack()
for i in range(st1.size() - 1):
    exchange(st1, stor1)
for i in range(stor1.size()):
    exchange(stor1, stor2)
exchange(st1, stor2)
print(st1)
print(stor1)
print(stor2)