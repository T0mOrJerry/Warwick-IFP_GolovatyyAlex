class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


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


n1 = Node("John")
n2 = Node("Adam")
n3 = Node("Adam")
n4 = Node("Dan")
n5 = Node("Richard")
n6 = Node("Simon")
n1.left_child = n2
n1.right_child = n6
n2.left_child = n3
n2.right_child = n4
n6.left_child = n5
printtree(n1)