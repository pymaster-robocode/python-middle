class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def compare(node, value):
        if node.value['score'] > value['score']:
            return False
        elif node.value['score'] < value['score']:
            return True
        return None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if not self.compare(node, value):
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif self.compare(node, value):
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def print_inorder(self):
        self._print_inorder(self.root)
        print()

    def _print_inorder(self, node):
        if node:
            self._print_inorder(node.left)
            print(node.value, end="\n")
            self._print_inorder(node.right)
