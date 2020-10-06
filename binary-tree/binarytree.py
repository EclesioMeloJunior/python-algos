class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, node: Node):
        self.root = self._add_on_root(self.root, node)

    def height(self) -> int:
        return self._tree_height(self.root)

    def _tree_height(self, root: Node) -> int:
        if root is None:
            return 0

        return max(self._tree_height(root.left), self._tree_height(root.right)) + 1

    def search(self, value: int) -> Node:
        return self._search_for(self.root, value)

    def _search_for(self, root: Node, value: int) -> Node:
        if root is None:
            return None

        if root.value == value:
            return root

        if root.value > value:
            return self._search_for(root.left, value)

        return self._search_for(root.right, value)

    def print_tree(self, type_print: int):
        if type_print == 1:
            self._print_inorder(self.root)
        if type_print == 2:
            self._print_preorder(self.root)
        if type_print == 3:
            self._print_postorder(self.root)
        if type_print == 4:
            self._print_reverse(self.root)

    def _add_on_root(self, root: Node, node: Node) -> Node:
        if root is None:
            return node

        if root.value > node.value:
            root.left = self._add_on_root(root.left, node)

        if root.value < node.value:
            root.right = self._add_on_root(root.right, node)

        return root

    def _print_inorder(self, root: Node):
        if root is None:
            return

        self._print_inorder(root.left)
        print(root.value)
        self._print_inorder(root.right)

    def _print_reverse(self, root: Node):
        if root is None:
            return

        self._print_reverse(root.right)
        print(root.value)
        self._print_reverse(root.left)

    def _print_preorder(self, root: Node):
        if root is None:
            return

        print(root.value)
        self._print_preorder(root.left)
        self._print_preorder(root.right)

    def _print_postorder(self, root: Node):
        if root is None:
            return

        self._print_postorder(root.left)
        self._print_postorder(root.right)
        print(root.value)

    def print_levels(self):
        self._print_levels_root(self.root)

    def _print_levels_root(self, root: Node):
        if root is None:
            return

        q = []

        q.append(root)

        while q:
            count = len(q)

            while count > 0:
                temp = q.pop(0)
                print(temp.value, end=' ')

                if temp.left:
                    q.append(temp.left)

                if temp.right:
                    q.append(temp.right)

                count -= 1

            print(' ')
