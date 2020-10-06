class Node:
    def __init__(self, value: int, bf: int = 0):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

        self.bf = bf
        self.height = 1



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

    def _get_height(self, root: Node) -> int:
        if root is None:
            return 0

        return root.height

    def _add_to_root(self, root: Node, n: Node) -> Node:
        if root is None:
            return n

        if root.value > n.value:
            subtree_left = self._add_to_root(root.left, n)

            root.left = subtree_left
            subtree_left.parent = root.left

        if root.value < n.value:
            subtree_right = self._add_to_root(root.right, n)

            root.right = subtree_right
            subtree_right.parent = root.right
        
        l_height = self._get_height(root.left)
        r_height = self._get_height(root.right)

        root.height = max(l_height, r_height) + 1
        root.bf = l_height - r_height

        return self._balance(root)


    def _balance(self, root: Node) -> Node:
        if root.bf == 2:
            if root.left.bf < 0:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
            else:
                return self._rotate_right(root)

        elif root.bf == -2:
            if root.right.bf > 0:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)
            else:
                return self._rotate_left(root)

        else:
            return root
