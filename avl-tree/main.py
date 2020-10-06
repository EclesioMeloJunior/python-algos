from avltree import Node, AVLTree

t = AVLTree()

n1 = Node(40)
n2 = Node(34)
n3 = Node(32)
n4 = Node(25)

t.add(n1)
t.add(n2)
t.add(n3)
t.add(n4)

t.print_inorder()
t.height()
