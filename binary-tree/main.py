from binarytree import BinaryTree, Node

tree = BinaryTree()

node1 = Node(6)
node2 = Node(4)
node3 = Node(7)

node4 = Node(2)
node5 = Node(5)
node6 = Node(1)

tree.add(node1)
tree.add(node2)
tree.add(node3)
tree.add(node4)
tree.add(node5)
tree.add(node6)

tree.print_levels()
print("=====")

tree.print_tree(1)
print("=====")
tree.print_tree(2)
print("=====")
tree.print_tree(3)
print("=====")
tree.print_tree(4)
print("=====")

search1 = tree.search(1)
search10 = tree.search(10)

print("Finding number 1:", search1.value)
print("Finding number 10:", tree.search(10))

print("Height of tree:", tree.height())
