class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.value, end=' ')
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            print(node.value, end=' ')
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value, end=' ')

# Example Usage
if __name__ == "__main__":
    bt = BinaryTree()
    for value in [5, 3, 7, 2, 4, 6, 8]:
        bt.insert(value)

    print("In-order Traversal: ", end='')
    bt.in_order_traversal(bt.root)  # Output: 2 3 4 5 6 7 8 
    print("\nPre-order Traversal: ", end='')
    bt.pre_order_traversal(bt.root)  # Output: 5 3 2 4 7 6 8 
    print("\nPost-order Traversal: ", end='')
    bt.post_order_traversal(bt.root)  # Output: 2 4 3 6 8 7 5
