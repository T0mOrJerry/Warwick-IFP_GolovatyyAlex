class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def tree_creation():
    li = input("Input a root for your tree: ").split()
    print()
    current_data = li[0]
    n = Node(current_data)
    tree = n
    buffer = [(current_data, n)]
    while buffer:
        t = buffer.pop(0)
        current_node = t[1]
        current_data = t[0]
        b = input(f"Type data for the left child of the node {current_data}\n(if it has no such child - type None): ")
        print()
        a = input(f"Type data for the right child of the node {current_data}\n(if it has no such child - type None): ")
        if a != 'None':
            n = Node(a)
            current_node.right_child = n
            buffer.append((a, n))
        if b != 'None':
            n = Node(b)
            current_node.left_child = n
            buffer.append((b, n))
        print()
        print()
    return tree


def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)


def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)


def printtree(root_node: Node, n=0):
    if root_node is not None:
        print('\t' * n + root_node.data)
        printtree(root_node.left_child, n + 1)
        printtree(root_node.right_child, n + 1)


# n1 = Node("John")
# n2 = Node("Adam")
# n3 = Node("Adam")
# n4 = Node("Dan")
# n5 = Node("Richard")
# n6 = Node("Simon")
# n1.left_child = n2
# n1.right_child = n6
# n2.left_child = n3
# n2.right_child = n4
# n6.left_child = n5
n1 = tree_creation()
printtree(n1)