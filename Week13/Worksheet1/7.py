from Stacks import Stack

st = Stack()
for i in range(int(input())):
    st.push(input())
for i in range(st.size()):
    print(st.pop(), end="")