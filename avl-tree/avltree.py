class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self._root: Node = None

    def add(self, n: Node):
        self._root = self._add_to_root(self._root, n)

    def print_inorder(self):
        self.print_recursive(self._root)

    def height(self):
        print(self._height_node(self._root))

    def _height_node(self, r: Node) -> int:
        if r is None:
            return 0

        return max(self._height_node(r.left), self._height_node(r.right)) + 1

    def print_recursive(self, r: Node):
        if r is None:
            return

        self.print_recursive(r.left)
        print(r.value)
        self.print_recursive(r.right)

    def _add_to_root(self, root: Node, n: Node) -> Node:
        if root is None:
            return n

        if root.value > n.value:
            root.left = self._add_to_root(root.left, n)

        if root.value < n.value:
            root.right = self._add_to_root(root.right, n)

        return root
