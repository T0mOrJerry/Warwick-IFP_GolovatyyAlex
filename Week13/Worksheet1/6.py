from Stacks import Stack


a = 'EAS*Y*QUE***ST***IO*N***'
# a = 'LA*STI*N*FIR*ST**OU*T******'
st = Stack()
for i in a:
    if i == '*':
        print(st.pop(), end="")
    else:
        st.push(i)