from Stacks import Stack

st = Stack()
for i in range(int(input())):
    st.push(input())
print(st)
print(st.multi_pop(3))
print(st)